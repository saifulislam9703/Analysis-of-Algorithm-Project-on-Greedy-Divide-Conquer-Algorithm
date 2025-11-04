#!/usr/bin/env python3
# eeg_merge_runtime_vs_n.py

import numpy as np
import pandas as pd
import glob
import os
import time
import matplotlib.pyplot as plt

# -------------------------------
# Load EEG CSVs
# -------------------------------
def load_eeg_csvs(folder_path):
    csv_files = sorted(glob.glob(os.path.join(folder_path, "*.csv")))
    arrays = []
    for f in csv_files:
        df = pd.read_csv(f)
        arrays.append(df.to_numpy(dtype=float))
    return arrays

# -------------------------------
# Merge strategies
# -------------------------------
def naive_merge(arrays):
    n, m = len(arrays), arrays[0].shape[1]
    out = np.full(m, -np.inf)
    for arr in arrays:
        arr = np.nan_to_num(arr, nan=-np.inf)
        for i in range(m):
            if arr[0, i] > out[i]:
                out[i] = arr[0, i]
    return out

def iterative_merge(arrays):
    arrays_np = np.vstack([np.nan_to_num(arr, nan=-np.inf) for arr in arrays])
    return np.maximum.reduce(arrays_np)

def dc_merge(arrays):
    if len(arrays) == 0:
        raise ValueError("No arrays to merge")
    if len(arrays) == 1:
        return np.nan_to_num(arrays[0], nan=-np.inf)
    mid = len(arrays) // 2
    left = dc_merge(arrays[:mid])
    right = dc_merge(arrays[mid:])
    return np.maximum(left, right)

# -------------------------------
# Experiment: runtime vs number of sensors
# -------------------------------
folder = "complete-eeg-dataset"  # change if needed
arrays_all = load_eeg_csvs(folder)
arrays_all = [arr if arr.ndim==1 else arr.reshape(1,-1) for arr in arrays_all]
max_n = len(arrays_all)

methods = {"Naive": naive_merge, "Iterative": iterative_merge, "D&C": dc_merge}

# Choose sensor counts to benchmark (powers of 2 or evenly spaced)
sensor_counts = list(range(1, max_n+1, max(1, max_n//10)))
runtimes = {name: [] for name in methods.keys()}

for n in sensor_counts:
    arrays = arrays_all[:n]
    for name, func in methods.items():
        start = time.time()
        _ = func(arrays)
        end = time.time()
        runtimes[name].append(end - start)
    print(f"Completed benchmarking for n={n} sensors")

# -------------------------------
# Plot: runtime vs number of sensors
# -------------------------------
plt.figure(figsize=(7,5))
for name in methods.keys():
    plt.plot(sensor_counts, runtimes[name], marker='o', label=name)
plt.xlabel("Number of sensors (n)")
plt.ylabel("Runtime (seconds)")
plt.title("EEG Merge Runtime vs Number of Sensors")
plt.yscale("log")
plt.xscale("log")
plt.grid(True, which="both", linestyle='--', alpha=0.7)
plt.legend()
plt.savefig("runtime_vs_sensors.png", dpi=150)
plt.show()
