# DSPIRA hardware

Design and fabrication files for the DSPIRA hydrogen-line low-noise amplifier, designed by Kevin Bandura at West Virginia University.
The amplifier serves the DSPIRA horn telescope at 1420 MHz.

Start with the [hardware guide](https://wvurail.org/dspira/hardware/) or the [amplifier construction lesson](https://wvurail.org/dspira/DetailedLNAInstructions).

## Find what you need

| Folder | Contents |
| --- | --- |
| [design](design/) | Readable schematic and editable Altium files |
| [fabrication](fabrication/) | Version 3 Gerber layers and drill file |
| [assembly](assembly/) | Parts ordering guide and component locations |
| [assembly/reference](assembly/reference/) | Earlier parts and assembly guides |
| [docs](docs/) | Design overview, original design memo, and file history |
| [licenses](licenses/) | Original notices for imported assembly material |

## Build an amplifier

1. Review the [version 3 schematic](design/amplifier-v3.pdf) and match the documents to your board revision.
2. Order components using the [revision 4 parts guide](assembly/parts-guide-v4.pdf).
3. Send the eight files in [fabrication/v3](fabrication/v3/) to your board manufacturer.
4. Follow the [construction lesson](https://wvurail.org/dspira/DetailedLNAInstructions), using the [component locations](assembly/component-locations.jpg).

The [design overview](docs/design-overview.md) explains the amplifier and remaining documentation work.
For commercial alternatives, see the [amplifier options lesson](https://wvurail.org/dspira/LNA).

## Names and contributions

Folders and ordinary files use lowercase names with hyphens.
Altium source names and fabrication extensions retain their tool conventions; see the [design notes](design/README.md).
The [file map](docs/file-map.json) lists earlier paths and their replacements.
Follow the [contribution guide](CONTRIBUTING.md) when updating a design or fabrication set.

Previously named `os_radio_astro_hw`. Keep that name unused so GitHub's repository redirects continue working.
See the [repository map](https://wvurail.org/dspira/repository-map/) for related projects.

Lessons belong in [dspira](https://github.com/WVURAIL/dspira).
Applications and processing code belong in [dspira-software](https://github.com/WVURAIL/dspira-software).

## Credits and licenses

Kevin Bandura designed the amplifier through WVU's DSPIRA Research Experiences for Teachers program.
The board design retains its [CC0 notice](LICENSE).
Imported assembly documents retain their separate [MIT notices](licenses/).
