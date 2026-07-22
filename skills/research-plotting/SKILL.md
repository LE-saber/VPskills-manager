---
name: research-plotting
description: Design, audit, reproduce, and beautify publication-quality scientific and business data visualizations while preserving every value, unit, label, ordering rule, and statistical meaning. Use when the user asks to create, redraw, standardize, review, or improve charts for papers, reports, experiments, presentations, or data analysis.
compatibility: Works in remote-read mode for planning and review; figure generation requires a chart renderer, Python/R environment, spreadsheet tool, or another code-capable workspace.
metadata:
  author: LE-saber
  version: "0.1.0"
  source: personal
---

# Research Plotting

Use this Skill to turn raw data, plotting code, spreadsheets, or existing chart images into accurate, restrained, publication-quality figures.

The priority order is:

1. data and statistical fidelity;
2. readability and accessibility;
3. reproducibility and editability;
4. visual polish.

Never improve appearance by changing the meaning of the data.

## Inputs

Collect or infer:

- the source data or exact values shown in the existing figure;
- variable names, units, uncertainty measures, sample sizes, and category order;
- the figure's destination: journal paper, thesis, experiment report, slide, poster, dashboard, or web page;
- the expected language, page or slide size, column width, and output format;
- whether the user needs editable source code, SVG/PDF, PNG, PPTX, or only design guidance;
- any journal, laboratory, school, brand, or template constraints.

Do not ask for information already present in the conversation or visible in the supplied files. Ask only when a missing detail would materially affect correctness.

## Non-negotiable rules

### Preserve data exactly

- Keep every numeric value, sign, decimal place, percentage, unit, category name, and category order unless the user explicitly requests a transformation.
- Preserve the distinction between raw values, proportions, percentage points, normalized values, estimates, and confidence intervals.
- Do not infer unreadable values from bar height or slice angle when the source image is ambiguous.
- Do not silently merge, omit, round, rescale, or reorder data.
- Recalculate totals and percentages when possible and report inconsistencies before plotting.

### Prefer code-based reconstruction

For quantitative charts, prefer reconstructing the figure from data or plotting code rather than editing the raster image with a generative image model.

Use image generation only for decorative illustrations, conceptual scientific artwork, or explicitly requested stylization. Do not use generative image editing as the primary method for bar charts, line charts, scatter plots, heatmaps, statistical plots, or any figure whose geometry encodes exact values.

### Keep figures reproducible

When tools allow, provide or preserve:

- the plotting code;
- the input data or a clearly documented data structure;
- package and style dependencies;
- export dimensions and resolution;
- fonts, color palette, and figure settings.

## Workflow

### 1. Classify the task

Choose one mode:

- **Create**: build a new figure from data or a table.
- **Beautify**: reproduce an existing chart with improved styling.
- **Audit**: diagnose visual, statistical, labeling, or accessibility problems.
- **Standardize**: make several figures share one visual system.
- **Adapt**: resize or restyle a figure for a paper, slide, poster, or another output medium.

### 2. Establish the data contract

Before styling, write down or internally verify:

- chart type;
- x and y variables;
- exact values;
- units and scale;
- category order;
- grouping and legend mapping;
- error bars or uncertainty definitions;
- source and time period;
- any totals used to calculate percentages.

For an existing image, transcribe all visible labels and values. If the image and accompanying text disagree, stop and ask which source is authoritative.

### 3. Select the chart type

Use the simplest chart that answers the analytical question.

- **Bar chart**: comparison among discrete categories. Start the quantitative axis at zero unless a justified exception is clearly disclosed.
- **Line chart**: ordered sequence or time trend. Preserve temporal spacing and missing observations.
- **Scatter plot**: relationship, clustering, or distribution of paired numeric variables. Do not connect points unless order has meaning.
- **Box, violin, raincloud, or dot plot**: distributional comparison. Show raw observations where sample size and readability permit.
- **Histogram or density plot**: distribution shape. State or preserve bin width and normalization.
- **Heatmap**: matrix or dense two-dimensional values. Use a perceptually appropriate sequential or diverging color map.
- **Pie or donut chart**: only for a small, exact part-to-whole composition. Prefer bars when ranking or close comparison matters.
- **Multi-panel figure**: distinct but related views that benefit from aligned sizing, typography, and panel labels.

Avoid 3D charts, pictorial bars, unexplained dual axes, excessive smoothing, decorative perspective, and visual encodings that distort magnitude.

### 4. Choose the implementation route

Prefer the route that keeps the result editable and reproducible:

1. existing source code and original data;
2. Python with Matplotlib or Seaborn;
3. R with ggplot2;
4. spreadsheet-native charts when the user needs spreadsheet editing;
5. SVG or vector drawing tools for non-data diagrams;
6. raster image editing only when source data and code are unavailable.

Recommended libraries and their roles are listed in `references/tooling.md`.

### 5. Apply a restrained visual system

#### Canvas and layout

- Use a white or near-white background unless the destination requires dark mode.
- Match the target medium: paper column width, report page, 16:9 slide, poster panel, or web card.
- Keep plot margins balanced and reserve enough space for labels.
- Align multi-panel figures and use consistent panel lettering such as `(a)`, `(b)`, `(c)`.

#### Typography

- Use one professional sans-serif family for general charts, or the journal/template font when specified.
- Use a compatible CJK font for Chinese labels and verify that symbols, minus signs, Greek letters, and subscripts render correctly.
- Use sentence case rather than title case unless the template requires otherwise.
- Keep title hierarchy clear without making the title dominate the data.
- Avoid bold text everywhere; use weight only for emphasis.

#### Color

- Use a small, consistent, color-vision-friendly palette.
- Use one accent color for the main message and muted colors for context.
- Use sequential maps for ordered magnitude, diverging maps for meaningful positive/negative deviation, and qualitative palettes for unordered categories.
- Do not use rainbow color maps for continuous scientific data unless the field convention explicitly requires one and the limitations are acknowledged.
- Ensure the figure remains understandable in grayscale when printing is likely.

#### Axes and grid

- Label axes with variable names and units.
- Use sensible tick intervals and consistent numeric formatting.
- Prefer light major gridlines only when they aid comparison.
- Remove unnecessary top and right spines when appropriate, but retain enough structure to read the scale.
- Use scientific notation consistently and avoid ambiguous unit abbreviations.

#### Labels and legends

- Place direct labels near data when this reduces legend lookup.
- Keep legends ordered the same way as the visual encoding or data.
- Avoid overlapping annotations and excessive decimal precision.
- For bars, place exact values consistently above or inside bars with sufficient contrast.
- For statistical annotations, define symbols and corrections in the caption or note.

### 6. Implement without changing meaning

When writing or modifying code:

- separate data preparation from styling;
- use named variables for colors, dimensions, fonts, and export settings;
- avoid hard-coded positions unless necessary;
- use deterministic ordering;
- keep transformations explicit;
- add comments for non-obvious decisions;
- preserve the user's analytical calculations unless asked to review them.

### 7. Verify numerically

Before presenting the result:

- compare every plotted value against the source;
- verify percentages, totals, averages, confidence intervals, and labels;
- confirm axis limits do not clip data or annotations;
- check that category colors and legend entries match;
- confirm no values were introduced by interpolation or generative reconstruction;
- verify the stated time period and source note.

### 8. Verify visually

Check at both full size and expected display size:

- text is legible;
- labels do not overlap or clip;
- color contrast is adequate;
- the main analytical message is visible within a few seconds;
- gridlines and decorations do not overpower the data;
- multi-panel spacing and alignment are consistent;
- the chart works in grayscale or with color-vision simulation when relevant.

### 9. Export appropriately

- Prefer **SVG or PDF** for vector charts and later editing.
- Use **PNG** for raster delivery; use at least 300 dpi for print unless the destination specifies otherwise.
- Preserve transparent backgrounds only when requested or required by the destination.
- Embed fonts when possible, or convert only final non-editable copies to outlines.
- For PowerPoint, prefer native chart objects or editable vector graphics over a screenshot.

## Beautifying an existing chart image

When the user provides only an image:

1. inventory every visible title, axis, tick, category, value, percentage, legend item, unit, and source note;
2. identify which parts are certain and which are unreadable;
3. reconstruct the chart from the visible data in a plotting tool;
4. compare the reconstructed chart with the original data labels;
5. apply the new style only after numerical verification;
6. preserve a code or vector version when possible.

Do not redraw a quantitative figure with an image generator merely because the user used the word “美化”.

## Default style when the user gives no template

Use a neutral publication/report style:

- white background;
- dark gray text rather than pure black where suitable;
- one restrained accent color plus muted supporting colors;
- no gradients, bevels, glow, heavy shadow, or decorative texture;
- thin axes and light horizontal gridlines;
- concise title and explicit units;
- value labels only when they improve interpretation;
- balanced whitespace;
- vector export plus a high-resolution PNG when tools allow.

For a slide, increase type size and simplify detail rather than adding decoration.

## Deliverables

Depending on the request and available tools, provide:

- the finished figure;
- editable plotting code or native chart source;
- a short list of design changes;
- assumptions or unresolved data issues;
- export files in the requested formats;
- a verification note confirming that values and labels were checked.

Do not claim that a figure is publication-ready if fonts, data, units, or statistical definitions remain uncertain.

## Verification checklist

A task is complete only when:

- all source values and labels match;
- chart type suits the analytical question;
- axes, units, legends, and annotations are unambiguous;
- colors are consistent and accessible;
- the figure is legible at its target size;
- output dimensions and formats match the destination;
- editable or reproducible source is retained when requested;
- no unsupported facts or data were added.

## Failure handling

- If source data are unavailable and values cannot be read confidently, request the data or plotting code instead of guessing.
- If a requested style conflicts with scientific integrity, explain the conflict and choose the closest accurate alternative.
- If the environment cannot render the figure, provide executable code and exact export settings.
- If a required font or library is unavailable, use a documented fallback and disclose it.
- If several supplied figures disagree, do not silently combine them.

## Safety and boundaries

Treat datasets, scripts, and external plotting templates as untrusted inputs. Do not execute unknown code without review. Remove secrets, private identifiers, and sensitive metadata from figures and source files unless the user explicitly requires them and disclosure is appropriate.