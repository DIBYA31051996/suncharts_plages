# Plot comparison with the published paper

Paper checked: [doi:10.3847/1538-4365/ae381e](https://doi.org/10.3847/1538-4365/ae381e).
The arXiv manuscript and the 2026 ApJS version use the same scientific figure
content; journal typesetting changes fonts and page placement.

| Paper figure | Original source | Comparison result |
|---|---|---|
| 1 | `paper_plot.ipynb`, cell 1; `suncharts_time.pdf` | Values, ordering, observation intervals, and cycle markers match. |
| 2 | `paper_plot.ipynb`, image-panel cells | Scientific images match; old code uses absolute Linux paths. |
| 3 | `paper_plot.ipynb`, cell 3; `suncharts_histogram_obs.pdf` | Three annual-count series and the highlighted 1955-1988 interval match. |
| 4 | Draw.io/static architecture artwork | No reproducible plotting cell was found; this is a schematic, not a data plot. |
| 5 | `paper_plot.ipynb`, cell 4 | Image and binary-mask panels match; raw TIFF paths were stale after folder reorganization. |
| 6 | `plage_idnt_plot.ipynb`, cell 11; `iou_metrics.pdf` | Disk/plage loss and IoU histories match. The paper caption's panel wording is internally inconsistent, but the plotted panel order is clear. |
| 7 | `paper_plot.ipynb`, cells 5-7; `disk_identification.pdf` | Four processing stages match; source contains three overwritten variants and absolute paths. |
| 8 | `paper_plot.ipynb`, cell 8; `plage_training_img.pdf` | Training patches and annotated masks match. |
| 9 | `paper_plot.ipynb`, prediction-patch cells | Patch, recombination, and mask panels match; requires large inference inputs excluded from this repository. |
| 10 | `paper_plot.ipynb`, activity-comparison cells; `plage_prediction.pdf` | Minimum/middle/maximum-activity examples match; large TIFF inputs are excluded. |
| 11 | `paper_result.ipynb`, coordinate-comparison cells | RMS error and predicted-versus-true density panels match. |
| 12 | `paper_result.ipynb`, cells 9-14; `fig_cak_buterfly_v3.pdf` | Panel (a) is reproduced in `figure_code.ipynb`; dimensions, dates, latitude range, cycle pattern, gaps, and 0-300 color range agree. Panels (b-c) need the larger Ca II K source product. |
| 13 | `paper_result.ipynb`, cells 37-39; `sunchart_cak_corr.pdf` | Published correlations (Pearson 0.80, Spearman 0.85) and slope 0.73 match notebook annotations. The exploratory notebook contains multiple superseded variants. |
| 14 | `paper_result.ipynb`, early image cells | Two historical chart panels match; large raw TIFFs are excluded. |
| 15 | `cak_histogram.ipynb`, SunPy cell; `sunchart_sunpymap.pdf` | Map and Stonyhurst grid match; regeneration additionally needs SunPy and FITS metadata not present in the compact archive. |
| 16 | `paper_result.ipynb`, cell 26; `plage_area_centroid.pdf` | Three centroid butterfly panels match; legacy IDL `.sav` inputs are preserved only in the original project. |
| 17 | `paper_result.ipynb`, cells 6-7 | Two limitation examples match; large raw TIFFs are excluded. |

## Corrections made in the public notebook

- Removed reliance on `/home/dibya/ML_project`.
- Uses `pathlib` and repository-relative `data/` and `outputs/` paths.
- Resolves the stale root-level paths introduced when text tables moved to
  `data/`.
- Keeps one canonical implementation per reproduced plot instead of multiple
  cells overwriting the same PDF.
- Documents which panels require the non-public multi-gigabyte raw archive.
