from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks" / "figure_code.ipynb"

nb = nbf.v4.new_notebook()
nb["metadata"]["kernelspec"] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
nb["metadata"]["language_info"] = {"name": "python", "version": "3"}

cells = [
    nbf.v4.new_markdown_cell(
        """# Figure code for Mishra et al. (2026)

Portable plotting code for the quantitative figures in
*Machine Learning-based Identification of the Solar Disk and Plages in
Kodaikanal Solar Observatory Historical Suncharts*,
[doi:10.3847/1538-4365/ae381e](https://doi.org/10.3847/1538-4365/ae381e).

The notebook uses repository-relative paths, writes plots to `outputs/`, and
documents the published comparison beside each reproducible figure."""
    ),
    nbf.v4.new_code_cell(
        """from pathlib import Path
import os

ROOT = Path.cwd()
if ROOT.name == "notebooks":
    ROOT = ROOT.parent
os.chdir(ROOT)

DATA = ROOT / "data"
OUTPUT = ROOT / "outputs"
OUTPUT.mkdir(exist_ok=True)

import h5py
import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

mpl.style.use(ROOT / "bkj_style.mplstyle")
mpl.rcParams["text.usetex"] = False
print(f"Repository root: {ROOT}")"""
    ),
    nbf.v4.new_markdown_cell(
        """## Figure 1 - temporal coverage

Comparison result: the notebook values and layout match the published figure.
The final journal version updates the caption typography during typesetting."""
    ),
    nbf.v4.new_code_cell(
        """observatories = {
    "Kislovodsk": (1979, 2021), "McIntosh": (1967, 2024),
    "Meudon": (1919, 2024), "SST": (1981, 2017),
    "ROB": (1940, 2011), "MWO": (1913, 2017),
    "KoSO": (1904, 2022), "Taipei": (1941, 2015),
    "YNAO": (1957, 2016), "Kanzelhohe": (1944, 2023),
    "Specola": (1947, 2004),
}
colors = {
    "Kislovodsk": "orchid", "McIntosh": "dodgerblue", "Meudon": "indianred",
    "SST": "orange", "ROB": "tomato", "MWO": "green", "KoSO": "crimson",
    "Taipei": "firebrick", "YNAO": "teal", "Kanzelhohe": "steelblue",
    "Specola": "deeppink",
}
ordered = sorted(observatories, key=lambda key: observatories[key][1] - observatories[key][0])
fig, ax = plt.subplots(figsize=(6, 3.2))
for name in ordered:
    start, end = observatories[name]
    left = datetime(start, 1, 1)
    right = datetime(end, 12, 31)
    ax.barh(name, right-left, left=left, color=colors[name], alpha=.5, height=.85)
    ax.text(left + (right-left)/2, name, f"({start}-{end})", ha="center", va="center", fontsize=6)
ax.set_xlim(datetime(1900, 1, 1), datetime(2024, 12, 31))
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.set_xlabel("Time [Years]")
ax.set_ylabel("Observatories")
fig.savefig(OUTPUT / "figure_01_temporal_coverage.pdf", dpi=300, bbox_inches="tight")
plt.show()"""
    ),
    nbf.v4.new_markdown_cell(
        """## Figure 3 - annual observing-day counts

Comparison result: series, highlighted 1955-1988 interval, colors, limits, and
legend agree with the paper. This cell fixes the old notebook's stale root-level
filenames by loading both tables from `data/`."""
    ),
    nbf.v4.new_code_cell(
        """cak = pd.read_csv(DATA / "KoSO_yearly_cak_observation.txt", sep=r"\\s+", index_col=0)
sunchart = pd.read_csv(DATA / "sunchart_hist.txt", sep=r"\\s+", index_col=0)
fig, ax = plt.subplots(figsize=(7, 2.7))
ax.bar(sunchart.index, sunchart.Nobs, label="Sunchart/Total", fill=False,
       edgecolor="maroon", linewidth=.5, width=.6)
ax.bar(sunchart.index, sunchart.NobsC, label="Sunchart/Plage",
       color="indianred", alpha=.65, width=.6)
ax.bar(cak.index, cak.NobsU, label="Ca-K", fill=False,
       edgecolor="navy", linewidth=.5, width=.6)
ax.axvspan(1955, 1988, color="orange", alpha=.1, ec="black")
ax.text(1971.5, 410, "(1955-1988)", ha="center", fontsize=8)
ax.text(.62, .86, "Suncharts > Ca-K", transform=ax.transAxes, ha="center", fontsize=8)
ax.set(xlim=(1900, 2020), ylim=(0, 500), xlabel="Time [Year]", ylabel="Counts")
ax.legend(frameon=False, ncol=2, fontsize=8)
fig.savefig(OUTPUT / "figure_03_observing_days.pdf", dpi=300, bbox_inches="tight")
plt.show()"""
    ),
    nbf.v4.new_markdown_cell(
        """## Figure 6 - loss and IoU

Comparison result: the stored training histories reproduce all four published
panels, including 25 disk epochs and 60 plage epochs."""
    ),
    nbf.v4.new_code_cell(
        """def history(path):
    with h5py.File(path, "r") as handle:
        attrs = handle["mask"].attrs
        return {key: np.asarray(attrs[key]) for key in
                ("epochs", "loss", "val_loss", "acc", "val_acc")}

disk = history(DATA / "iou_disk_idnt.h5")
plage = history(DATA / "iou_plage_idnt.h5")
fig, axes = plt.subplots(2, 2, figsize=(6, 5), sharey="row")
for col, (item, title) in enumerate(((disk, "Disk Detection"), (plage, "Plage Detection"))):
    axes[0, col].plot(item["epochs"], item["loss"], color="darkgoldenrod", label="Training loss")
    axes[0, col].plot(item["epochs"], item["val_loss"], color="indianred", label="Validation loss")
    axes[1, col].plot(item["epochs"], item["acc"], color="darkgoldenrod", label="Training IoU")
    axes[1, col].plot(item["epochs"], item["val_acc"], color="indianred", label="Validation IoU")
    axes[0, col].set_title(title)
    axes[1, col].set_xlabel("Epochs")
    axes[0, col].legend(frameon=False, fontsize=7)
    axes[1, col].legend(frameon=False, fontsize=7)
axes[0, 0].set_ylabel("Loss")
axes[1, 0].set_ylabel("IoU")
axes[1, 0].set_ylim(0, 1)
for label, ax in zip(("a", "b", "c", "d"), axes.ravel()):
    ax.text(.04, .9, f"({label})", transform=ax.transAxes)
fig.tight_layout()
fig.savefig(OUTPUT / "figure_06_training_history.pdf", dpi=300, bbox_inches="tight")
plt.show()"""
    ),
    nbf.v4.new_markdown_cell(
        """## Figure 12(a) - sunchart plage butterfly diagram

This is the figure backed by the online HDF5 data product. The paper states that
the map covers 1916-2007, uses 1-degree latitude bins, averages multiple daily
observations, and reports area in millionths of the solar disk fraction.

Comparison result: dates, latitude extent, solar-cycle structure, color scale
(0-300 micro-disk fractions), and data gaps agree with panel (a) of Figure 12."""
    ),
    nbf.v4.new_code_cell(
        """with h5py.File(DATA / "KoSO_sunchart_plage_butterfly.h5", "r") as handle:
    area = np.asarray(handle["mask_area"])
    dates = pd.to_datetime([
        item.decode() if isinstance(item, bytes) else item
        for item in handle["dates"][:]
    ])

# The archived file has observations on rows and 181 latitude bins on columns.
if area.shape[0] == len(dates):
    area = area.T
latitudes = np.linspace(-90, 90, area.shape[0])
print(f"shape={area.shape}; dates={dates.min().date()} to {dates.max().date()}")

fig, ax = plt.subplots(figsize=(9, 3.2))
mesh = ax.pcolormesh(dates, latitudes, area, shading="auto",
                     cmap="turbo", vmin=0, vmax=300, rasterized=True)
ax.set(xlabel="Time [Years]", ylabel="Latitude [deg]", ylim=(-75, 75))
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
colorbar = fig.colorbar(mesh, ax=ax, pad=.02)
colorbar.set_label("Plage Area [micro-DF]")
fig.savefig(OUTPUT / "figure_12a_sunchart_butterfly.pdf", dpi=300, bbox_inches="tight")
plt.show()"""
    ),
    nbf.v4.new_markdown_cell(
        """## Original research notebooks

The full exploratory notebooks are preserved in `notebooks/source/`. They are
included for provenance, but many contain training/inference cells that require
the private multi-gigabyte raw-image archive. See `PLOT_COMPARISON.md` for the
figure-by-figure mapping and the known differences found during review."""
    ),
]

nb["cells"] = cells
nbf.write(nb, OUT)
print(OUT)
