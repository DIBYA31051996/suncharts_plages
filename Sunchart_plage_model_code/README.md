# Kodaikanal Sunchart Analysis

This repository contains exploratory notebooks, trained models, and IDL save
files used to detect the solar disk and segment plages in Kodaikanal hand-drawn
suncharts.

## Repository contents

| File | Purpose |
| --- | --- |
| `solar_disk_circle_detection.ipynb` | Post-process limb masks with circle detection. |
| `solar_disk_center_training.ipynb` | Train a CNN to locate the solar disk. |
| `solar_limb_model_inference.ipynb` | Load the limb model and generate predictions. |
| `plage_segmentation_training.ipynb` | Train plage segmentation from manually labelled charts. |
| `sunchart_plage_inference.ipynb` | Run plage inference and save processed products. |
| `solar_disk_geometry_catalog.txt` | Disk centre, radius, and position-angle catalogue. |
| `solar_limb_segmentation_model.h5` | Trained limb segmentation model. |
| `sunchart_plage_segmentation_model.h5` | Trained plage segmentation model. |
| `feature_availability_*.sav` | Annual feature-availability counts for 1904–2022. |

## Data paths

The notebooks document the original absolute data paths used during
development. Before running a notebook on another machine, change its
configuration cell to point to local image, mask, model, and output
directories. Large source image collections are not included here.

## IDL save files

Each `.sav` file has four aligned arrays:

- `years`: calendar year;
- `n_charts`: number of available charts;
- `n_kodai`: charts containing the named feature in Kodaikanal data;
- `n_other`: charts containing the feature in another source.



## Environment

The notebooks were developed with Python, TensorFlow/Keras, OpenCV, NumPy,
SciPy, scikit-image, Pillow, Matplotlib, tifffile, h5py, and patchify. Exact
TensorFlow and CUDA versions depend on the available GPU and should be pinned
for the target machine before reproducing model training.

