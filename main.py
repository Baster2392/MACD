import getting_data as data
import macd
import plot

if __name__ == '__main__':
    samples = data.get_samples()
    clos = [sample[1] for sample in samples]
    dates = [sample[0] for sample in samples]
    macds = macd.get_macds(clos)
    signals = macd.get_signals(macds)
    plot.plot(dates, macds, signals)


