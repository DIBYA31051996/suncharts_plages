import pandas as pd
import h5py
import numpy as np

# Input and output paths
txt_path = "/home/dibya/ML_project/filtered_sunchart_mask_area.txt"
h5_path  = "/home/dibya/ML_project/KoSO_sunchart_plage_butterfly.h5"

# --- Load and process the data ---
# Assumes: first column = date, rest = values
data = pd.read_csv(
    txt_path,
    header=None,
    delimiter=r"\s+",
    index_col=0
)

# Convert index to datetime
data.index = pd.to_datetime(data.index)

# Resample to daily cadence (sum per day)
datar = data.resample("D").sum()

# --- Save to HDF5 ---
with h5py.File(h5_path, "w") as f:
    # Save numeric data
    f.create_dataset("mask_area", data=datar.values)

    # Save dates as ISO strings
    date_str = datar.index.strftime("%Y-%m-%dT%H:%M").to_numpy(dtype="S16")
    f.create_dataset("dates", data=date_str)

print(f"Saved HDF5 file to: {h5_path}")
print("Dataset shape:", datar.shape)

