# Hydrogen-line amplifier

The amplifier boosts weak 21 cm signals from the telescope's antenna probe before they reach the receiver.
It connects through an SMA connector and should sit close to the probe.
This filtered design was developed for use in urban environments.

## Components and revision

The [version 3 schematic](../design/amplifier-v3.pdf) is dated August 18, 2017.
The component census below comes from the Altium schematic source.

| Quantity | Part | Role |
| --- | --- | --- |
| 1 | SAV-541 | Front-end low-noise transistor |
| 2 | GALI 39+ | Mini-Circuits MMIC gain blocks |
| 2 | BFCN-1445 | Mini-Circuits bandpass filters, centered near 1445 MHz |
| 1 | LM2940 | Low-dropout 5 V regulator in SOT-223, with DC fed over the RF output |

The signal chain has three gain stages and two filters.
Passives use 0603 packages, with 1% tolerance where marked.

The schematic includes these GALI 39+ annotations:

- NF = 2.4 dB
- IP3 = 23 dBm
- S21 = 21 dB

They do not describe the SAV-541 front end, which determines the first-stage noise contribution.
Consult the SAV-541 datasheet when evaluating that device.

## Earlier design notes

The [2017 memo](amplifier-design-2017.pdf) records the original rationale and measurements.
An [editable Word copy](amplifier-design-2017.docx) uses the current WVU DSPIRA document template.
The [earlier assembly references](../assembly/reference/) explain institute builds.
Their component choices, bias settings, and cost estimates are historical.
Match those documents to your actual board revision.

The schematic PDF keeps the original drawing scale, with the header and page numbers outside the drawing area.
Print it at actual size when scale matters.

## Bill of materials

A machine-readable `bom.csv` is not yet included.
Export one from the [Altium schematic](../design/altium/HI_Amplifer_schematic.SchDoc) using **Reports → Bill of Materials**.
Verify component values and quantities before publishing it.
Use the [revision 4 parts guide](../assembly/parts-guide-v4.pdf) for the current lesson's ordering reference.
