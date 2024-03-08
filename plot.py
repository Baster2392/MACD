import matplotlib.pyplot as pyplot


def plot(dates, macds, signals):
    pyplot.plot(dates, macds)
    pyplot.plot(dates, signals)

    pyplot.xlabel("Time")
    pyplot.ylabel("MACD")

    pyplot.xticks([dates[i] for i in range(0, len(dates), 50)], rotation=45)

    pyplot.title("MACD")
    pyplot.show()

