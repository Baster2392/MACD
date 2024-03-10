import matplotlib.pyplot as pyplot


def plot_macd(dates, macds, signals):
    pyplot.plot(dates, macds, label="MACD")
    pyplot.plot(dates, signals, label="SIGNAL")

    pyplot.legend()
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
    pyplot.title("Stock prices")
    pyplot.show()

