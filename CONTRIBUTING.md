# Contributing

Keep board designs, fabrication files, and amplifier assembly references here.
Send classroom lessons to [dspira](https://github.com/WVURAIL/dspira).
Send software to [dspira-software](https://github.com/WVURAIL/dspira-software).

## File organization

- Put editable board files and readable schematics in `design/`.
- Put each fabrication revision in its own `fabrication/vN/` folder.
- Keep fabrication folders limited to the files a board manufacturer needs.
- Put current parts guides and component images in `assembly/`.
- Keep earlier assembly documents in `assembly/reference/`, with their revision or date in the name.
- Put design explanations in `docs/` and record import details in the commit description.
- Preserve author credits and license notices when importing material.

Use descriptive lowercase names with hyphens.
Keep conventional Altium and Gerber extensions.
The existing Altium filenames are an exception because the PCB embeds references to the schematic name.
Rename those sources only within an Altium project that updates and verifies those associations.

## Before publishing

Include the board revision, editable sources, fabrication outputs, and any new measurements.
Review copper layers, solder masks, silkscreens, board outline, and drill data together after a design change.
Export a matching schematic PDF when updating the editable sources.

For file moves, verify that the design and fabrication bytes remain unchanged.
Add old-to-new paths to `docs/file-map.json` and update affected links in the `dspira` website.

A machine-readable bill of materials is still needed.
Export it from Altium and verify it against the schematic and parts guide before publishing it.
