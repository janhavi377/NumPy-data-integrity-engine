import numpy as np

def find_missing(data):
    # Count NaNs per column
    return np.isnan(data).sum(axis=0)

def detect_outliers_zscore(data, threshold=3):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    z_scores = (data - mean) / std
    return np.abs(z_scores) > threshold

