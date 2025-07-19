import numpy as np

from loader import load_data
from validator import find_missing, detect_outliers_zscore
from transformer import replace_missing, normalize_minmax



def run_pipeline(file_path):
    data, columns = load_data(file_path)
    print("Columns:", columns)
    print("Initial data:\n", data)

    print("\nMissing values per column:", find_missing(data))
    data = replace_missing(data)
    print("\nData after missing value replacement:\n", data)

    outliers = detect_outliers_zscore(data)
    print("\nOutliers detected at positions:\n", np.where(outliers))

    data = normalize_minmax(data)
    print("\nNormalized data:\n", data)

if __name__ == "__main__":
    # run_pipeline("data/sample_data.csv")
    run_pipeline("../data/sample_data.csv")


