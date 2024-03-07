import pandas as pd


def get_samples():
    samples = pd.read_csv("data/wig20_d.csv")

    # extract essential data
    dates = samples.iloc[:, 0]
    closings = samples.iloc[:, 4]
    return list(zip(dates, closings))
