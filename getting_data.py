import pandas as pd


def get_samples():
    samples = pd.read_csv("data/gold.csv")

    # extract essential data
    dates = samples.iloc[:, 0]
    closings = samples.iloc[:, 4]
    samples = list(zip(dates, closings))
    return samples
