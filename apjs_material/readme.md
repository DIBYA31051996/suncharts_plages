1. File Overview

KoSO_sunchart_plage_butterfly.h5 contains the daily plage area time–latitude data used to generate Fig. 12(a) in the paper:
“Machine Learning Based Identification of Solar Disk and Plages in Kodaikanal Solar Observatory Historical Suncharts.”

This dataset represents plage areas extracted automatically from the Kodaikanal Solar Observatory (KoSO) suncharts using a U-Net–based machine-learning segmentation model. The data cover the period 1916–2007, corresponding to solar cycles 15–23.

2. Scientific Description

Each daily map provides the plage area (in μDF: millionths of the solar disk fraction) binned into 1° latitude strips, ranging from −90° to +90°.
If multiple sunchart images were available for the same day, plage areas were averaged.

This dataset forms the basis of the time–latitude butterfly diagram shown in:

Fig. 12(a) — Current work (U-Net–based sunchart plage detection)



3. File Structure

The HDF5 file contains two datasets:

(a) mask_area

Type: 2D float array
Shape: (N_latitudes, N_days)
Units: μDF (millionths of disk fraction)
Latitude range: −90° to +90°, binned at 1°

Values represent daily averaged plage area per latitude bin

(b) dates

Type: 1D string array
ISO8601 format: "YYYY-MM-DDTHH:MM"
Length: N_days





4. Data Usage and Purpose

This dataset is intended for:

Solar cycle studies
Long-term chromospheric variability analysis
Comparison with Ca II K–based plage area
Reconstruction of missing plage activity in degraded KoSO years
Building composite time–latitude series


