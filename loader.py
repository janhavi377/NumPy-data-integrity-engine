import numpy as np
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df.to_numpy(), df.columns.to_numpy()



