import matplotlib.pyplot as pyplot


def plot_macd(dates, macds, signals):
    pyplot.plot(dates, macds)
    pyplot.plot(dates, signals)

    pyplot.xlabel("Time")
    pyplot.ylabel("MACD")

    pyplot.xticks([dates[i] for i in range(0, len(dates), 50)], rotation=45)

    pyplot.title("MACD")
    pyplot.show()


def plot_raw_data(dates, values):
    pyplot.plot(dates, values)
    pyplot.xlabel("Time")
    pyplot.ylabel("Prices")

    pyplot.xticks([dates[i] for i in range(0, len(dates), 50)], rotation=45)
    pyplot.title("Stocks prices")
    pyplot.show()

