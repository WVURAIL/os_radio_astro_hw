"""Check repository integrity without validating circuit behavior or fabrication suitability."""
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def local_file(value):
    path = (ROOT / value).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file() or path.stat().st_size == 0:
        raise ValueError(f"Missing, empty, or unsafe file: {value}")
    return path


def check():
    mapping = json.loads((ROOT / "docs/file-map.json").read_text())
    if not mapping.get("files"):
        raise ValueError("The historical file map is empty")
    for current in mapping["files"].values():
        local_file(current)

    pdfs = sorted(ROOT.glob("**/*.pdf"))
    for path in pdfs:
        reader = PdfReader(path, strict=True)
        if reader.is_encrypted or len(reader.pages) == 0:
            raise ValueError(f"PDF is encrypted or has no pages: {path}")
        for page in reader.pages:
            if float(page.mediabox.width) <= 0 or float(page.mediabox.height) <= 0:
                raise ValueError(f"Invalid PDF page dimensions: {path}")
            page.get_contents()

    documents = sorted(ROOT.glob("**/*.docx"))
    for path in documents:
        local_file(path.with_suffix(".pdf").relative_to(ROOT))
        with ZipFile(path) as archive:
            if archive.testzip() is not None:
                raise ValueError(f"Corrupt Word archive: {path}")
            ET.fromstring(archive.read("word/document.xml"))
    for folder in ("assembly", "docs"):
        for path in (ROOT / folder).rglob("*.pdf"):
            local_file(path.with_suffix(".docx").relative_to(ROOT))

    layers = {"GBL", "GBO", "GBS", "GKO", "GTL", "GTO", "GTS", "TXT"}
    expected = {f"amplifier-v3.{extension}" for extension in layers}
    actual = {path.name for path in (ROOT / "fabrication/v3").iterdir() if path.is_file()}
    if actual != expected:
        raise ValueError(f"Incomplete or unexpected v3 fabrication set: {actual ^ expected}")
    for filename in sorted(expected):
        text = local_file(f"fabrication/v3/{filename}").read_text(encoding="ascii")
        if filename.endswith(".TXT"):
            if not text.startswith("M48") or "M30" not in text:
                raise ValueError(f"Missing drill header or end marker: {filename}")
        elif "%FS" not in text or not re.search(r"M02\*", text):
            raise ValueError(f"Missing Gerber format or end marker: {filename}")
    print(f"Validated {len(mapping['files'])} mapped paths, {len(pdfs)} PDFs, "
          f"{len(documents)} document pairs, and {len(expected)} fabrication files.")
    print("Electrical, dimensional, BOM, and manufacturing review remain manual.")


if __name__ == "__main__":
    check()
