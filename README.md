# DSPIRA Hydrogen-Line LNA (`os_radio_astro_hw`)

Open hardware design files for the **DSPIRA low-noise amplifier** — a 1420 MHz
preamplifier for neutral hydrogen (21 cm) observations, designed by
**Kevin Bandura** (WVU LCSEE) for the DSPIRA horn telescope.

> ⚠️ **This repository is linked from published DSPIRA curriculum.**
> The lesson [*Low Noise Amplifier (LNA) Options*](https://wvurail.org/dspira-lessons/LNA)
> points teachers here to obtain fabrication files. **Do not delete or transfer this
> repository out of the organization** — either action breaks that link. (Renaming is
> safe; GitHub preserves redirects for renames.)

## What this is for

The LNA is the most critical component of the horn telescope. It amplifies the extremely
weak 21 cm signal and must sit as close to the antenna probe as possible, so that noise
picked up downstream is not amplified along with the signal. It connects to the probe
through a standard SMA connector.

This design was intended to work in **urban environments**, where a filtered front end
matters more than it does at a quiet site. Approximate build cost is **$60**.

## Design summary

Signal chain, per the schematic (`Neutral_Hydrogen_amplifier_v3.pdf`):

Component census, taken directly from the Altium schematic source:

| Qty | Part | Role |
|---|---|---|
| 1 | **SAV-541** | Front-end low-noise transistor. As the first active device, its noise figure is what sets the system noise temperature. |
| 2 | **GALI 39+** | Mini-Circuits MMIC gain blocks |
| 2 | **BFCN-1445** | Mini-Circuits bandpass filters, centred near 1445 MHz |
| 1 | **LM2940** | Low-dropout 5 V regulator (SOT-223); DC fed over the RF output, bias-tee style |

So: three gain stages and two filters, not a single amplify-then-filter chain.

The schematic annotates **NF = 2.4 dB, IP3 = 23 dBm, S21 = 21 dB** twice, against the
GALI 39+ stages — those figures describe the gain blocks, **not** the SAV-541 front end.
For the front-end noise figure, which is the number that actually matters for a
low-noise amplifier, read the SAV-541 datasheet rather than trusting any summary here.

Passives are **0603** surface-mount throughout, 1% tolerance where marked.
Board revision **v3**, dated 2017-08-18.

## Files

| Path | What it is |
|---|---|
| `Neutral_Hydrogen_amplifier_v3.pdf` | **Readable schematic.** Start here — this is the only file viewable without commercial software. |
| `HI_Amplifer_schematic.SchDoc` | Altium schematic source (binary). *(Filename typo "Amplifer" is historical — kept so existing links don't break.)* |
| `HI_Amplifier.PcbDoc` | Altium PCB layout source (binary) |
| `HI_amp_v3_gerbers/` | **Fabrication files.** Gerber layers + NC drill (`.TXT`). Send this folder to a board house as-is. |

### Why Gerbers are committed

Gerbers are normally build output and would be excluded from version control. Here they
are **the deliverable** — a teacher following the lesson needs to download and send them
to a fab without owning Altium. Please leave them tracked.

### Gerber layer key

| Extension | Layer |
|---|---|
| `.GTL` / `.GBL` | Top / bottom copper |
| `.GTS` / `.GBS` | Top / bottom solder mask |
| `.GTO` / `.GBO` | Top / bottom silkscreen |
| `.GKO` | Board outline (keep-out) |
| `.TXT` | NC drill file |

## Building one

1. **Order the parts.** The authoritative bill of materials — with suppliers and part
   numbers — is the ordering guide on the lessons site:
   [LNA Ordering Parts Info (PDF)](https://wvurail.org/dspira-lessons/FilesUploaded/LNA_OrderingParts_Info_4.pdf)
2. **Fabricate the board.** Send `HI_amp_v3_gerbers/` to any PCB house.
3. **Assemble it.** Full step-by-step soldering instructions, with photos and video for
   each component type, are in
   [Detailed LNA Construction Instructions](https://wvurail.org/dspira-lessons/DetailedLNAInstructions).
4. **Coat it.** Apply silicone conformal coating after soldering, to protect against
   moisture, dust, and static discharge.

> 📋 **TODO for a maintainer:** a machine-readable `bom.csv` should live in this repo so
> the design is self-contained if the lessons-site PDF ever moves. Altium can export one
> directly from `HI_Amplifer_schematic.SchDoc` (Reports → Bill of Materials). This was
> deliberately *not* transcribed by hand from the schematic PDF — the risk of a wrong
> value sending someone's parts order sideways is not worth it.

## Alternatives to building your own

The lessons page also lists commercial options if hand-soldering 0603 parts is not
practical for your group:

- Nooelec SAWbird+ H1 (~$45)
- GPIO Labs Hydrogen Line LNA with bias tee (~$54)

## Related

- [DSPIRA lessons portal](https://wvurail.org/dspira-lessons/) — the curriculum this hardware serves
- [Building the Horn Telescope](https://wvurail.org/dspira-lessons/BuildingHornTelescope_Overview)

## Licence

See [`LICENSE`](LICENSE) — **CC0 1.0**: the design files are dedicated to the
public domain. Build it, modify it, sell boards, no permission needed.

If this design is ever substantially revised, a purpose-built hardware licence —
CERN-OHL-P (permissive) or CERN-OHL-S (reciprocal) — is worth considering, as it
speaks directly to fabrication outputs and the right to manufacture.

## Credits

Designed by Kevin Bandura, West Virginia University, Lane Department of Computer Science
and Electrical Engineering. Developed under the **DSPIRA** NSF Research Experiences for
Teachers (RET) programme.
