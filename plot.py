import matplotlib.pyplot as pyplot


def plot_macd(dates, macds, signals):
    pyplot.plot(dates, macds, label="MACD")
    pyplot.plot(dates, signals, label="SIGNAL")

    buy_dates = []
    sell_dates = []
    buy_points = []
    sell_points = []

    for i in range(len(dates)):
        # buy actions
        if signals[i - 1] > macds[i - 1] and signals[i] < macds[i]:
            buy_dates.append(dates[i])
            buy_points.append(macds[i])
        # sell actions
        if signals[i - 1] < macds[i - 1] and signals[i] > macds[i]:
            sell_dates.append(dates[i])
            sell_points.append(macds[i])

    pyplot.scatter(buy_dates, buy_points, color='red', zorder=5, label="Buy actions")
    pyplot.scatter(sell_dates, sell_points, color='blue', zorder=5, label="Sell actions")

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

