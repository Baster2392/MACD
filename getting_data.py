import pandas as pd


def get_samples(path, dates_index, values_index):
    samples = pd.read_csv(path)

    # extract essential data
    dates = samples.iloc[:, dates_index]
    closings = samples.iloc[:, values_index]
    samples = list(zip(dates, closings))
    return samples
