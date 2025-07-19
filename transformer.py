import numpy as np

def replace_missing(data, method="mean"):
    if method == "mean":
        col_means = np.nanmean(data, axis=0)
        idxs = np.where(np.isnan(data))
        data[idxs] = np.take(col_means, idxs[1])
    return data

def normalize_minmax(data):
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    return (data - min_val) / (max_val - min_val + 1e-8)

