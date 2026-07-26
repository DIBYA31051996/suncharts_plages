# KoSO sunchart plage figures

Reproducibility material for:

> D. K. Mishra et al., "Machine Learning-based Identification of the Solar
> Disk and Plages in Kodaikanal Solar Observatory Historical Suncharts,"
> *The Astrophysical Journal Supplement Series* 283, 19 (2026).
> [doi:10.3847/1538-4365/ae381e](https://doi.org/10.3847/1538-4365/ae381e)

The repository's original README is preserved unchanged in
[`README_ORIGINAL.md`](README_ORIGINAL.md).

Start with [`notebooks/figure_code.ipynb`](notebooks/figure_code.ipynb). It
reproduces Figures 1, 3, 6, and the online-data panel Figure 12(a), using
repository-relative paths.

## Layout

- `notebooks/figure_code.ipynb`: clean, portable figure notebook.
- `notebooks/source/`: original exploratory notebooks retained for provenance.
- `data/`: compact inputs required by `figure_code.ipynb`.
- `figures/reference/`: author-generated figure files used for comparison.
- `outputs/`: generated figures (ignored except for its placeholder).
- `PLOT_COMPARISON.md`: figure-by-figure audit against the paper.

## Run

```bash
python -m pip install -r requirements.txt
jupyter lab notebooks/figure_code.ipynb
```

Run the cells from top to bottom. The generated PDFs are written to `outputs/`.

## Data scope

The original project contains several gigabytes of scanned TIFF files and model
artifacts, including individual files above GitHub's normal 100 MB object
limit. Those files are not duplicated here. The repository includes the
compact tables, training histories, published figure references, and the
46.7 MB HDF5 online data product needed for the public figure workflow.

The HDF5 file contains:

- `mask_area`: daily plage area by 1-degree latitude bin, in millionths of the
  solar disk fraction.
- `dates`: ISO-8601 observation dates.

The data span 1916-2007 and cover solar cycles 15-23.
