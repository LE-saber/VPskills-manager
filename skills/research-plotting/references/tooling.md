# Research plotting tooling reference

Use this file only after selecting `research-plotting`. Tool availability and APIs can change, so verify current documentation before installing or relying on a specific option.

## Python

### Matplotlib

Use as the base plotting system when exact geometry, export control, and reproducibility matter. It is suitable for most publication figures and supports SVG, PDF, and high-resolution PNG output.

### Seaborn

Use for concise statistical graphics built on Matplotlib, especially distributions, categorical comparisons, regression views, and matrix plots. Keep styling restrained and verify all automatically computed summaries.

### SciencePlots

Repository: `garrettj403/SciencePlots`

Use for publication-oriented Matplotlib style sheets such as scientific and IEEE-like defaults. Treat it as a style layer, not a substitute for checking dimensions, fonts, labels, and data. On systems without a working LaTeX installation, use an appropriate non-LaTeX configuration.

### tueplots

Repository: `pnkraemer/tueplots`

Use to control figure dimensions, font sizes, and layout for paper columns or conference templates. It is particularly useful when charts must fit exact single-column or double-column widths.

### Colorcet

Repository: `holoviz/colorcet`

Use for perceptually designed continuous, diverging, and categorical color maps. It is useful for heatmaps, fields, dense scatter plots, and many-category visualizations.

### Matplotx

Repository: `nschloe/matplotx`

Use for selected Matplotlib enhancements such as direct line labels and additional styles. Adopt only the features that improve interpretation.

## R

### ggplot2

Use as the default grammar-of-graphics system for reproducible statistical figures.

### ggsci

Repository: `nanxstats/ggsci`

Use for restrained palettes inspired by scientific journals and organizations. A palette name does not itself make a figure compliant with a journal.

### ggpubr

Repository: `kassambara/ggpubr`

Use for common publication-oriented helpers and statistical annotations. Verify tests, p-values, correction methods, and annotation meanings independently.

### patchwork

Repository: `thomasp85/patchwork`

Use to compose multiple ggplot figures into aligned multi-panel layouts.

### ggprism

Repository: `csdaw/ggprism`

Use when a restrained GraphPad Prism-like presentation is appropriate for experimental or biomedical figures.

## Choosing among tools

- Use Matplotlib or ggplot2 when long-term reproducibility is the main requirement.
- Add SciencePlots for a quick publication-style baseline.
- Add tueplots when exact paper dimensions matter.
- Add Colorcet or another validated palette library when continuous color encoding is central.
- Use patchwork or Matplotlib layout tools for multi-panel figures.
- Use spreadsheet charts only when the user needs spreadsheet-native editing.
- Use SVG or diagram tools for conceptual figures whose geometry does not encode measured values.

## Installation caution

Do not install packages or execute repository scripts merely because they are referenced here. Installation and code execution require the user's current authorization and a review of the source, version, and environment.