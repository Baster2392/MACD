import getting_data as data
import macd
import plot

if __name__ == '__main__':
    path = input("Path do .csv file: ")
    dates_index = int(input("Index of column containing dates: "))
    values_index = int(input("Index of column containing values: "))
    funds = input("Start funds: ")
    dates_index = 0
    values_index = 4
    funds = 1000

    samples = data.get_samples(path, dates_index, values_index)
    clos = [sample[1] for sample in samples]
    dates = [sample[0] for sample in samples]

    macds = macd.get_macds(clos)
    signals = macd.get_signals(macds)

    plot.plot_raw_data(dates, clos)
    macd.analyze_macd(dates, macds, signals, clos, funds)
    plot.plot_macd(dates, macds, signals)


