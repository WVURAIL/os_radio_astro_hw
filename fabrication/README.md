# Board fabrication

[Version 3](v3/) contains seven Gerber layers and one NC drill file for the existing amplifier board.
The shared filename is `amplifier-v3`; uppercase extensions identify the layers.
The file contents are unchanged from the original fabrication set.

| File | Layer or purpose |
| --- | --- |
| [amplifier-v3.GTL](v3/amplifier-v3.GTL) | Top copper |
| [amplifier-v3.GBL](v3/amplifier-v3.GBL) | Bottom copper |
| [amplifier-v3.GTS](v3/amplifier-v3.GTS) | Top solder mask |
| [amplifier-v3.GBS](v3/amplifier-v3.GBS) | Bottom solder mask |
| [amplifier-v3.GTO](v3/amplifier-v3.GTO) | Top silkscreen |
| [amplifier-v3.GBO](v3/amplifier-v3.GBO) | Bottom silkscreen |
| [amplifier-v3.GKO](v3/amplifier-v3.GKO) | Board outline, exported from the keep-out layer |
| [amplifier-v3.TXT](v3/amplifier-v3.TXT) | NC drill data |

Download the [repository ZIP](https://github.com/WVURAIL/dspira-hardware/archive/refs/heads/main.zip) and extract it.
If your manufacturer requests a ZIP, zip the eight files inside `fabrication/v3/` together.
Keep this complete set together and match it to the [version 3 schematic](../design/amplifier-v3.pdf).

Fabrication outputs remain tracked so builders can order boards without owning Altium.
The files use the board design's [CC0 notice](../LICENSE).
