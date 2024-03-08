def calculate_ema(samples, measures):
    alpha = 2 / (measures + 1)
    sum1 = 0
    sum2 = 0

    for i in range(measures - 1, -1, -1):
        weight = (1 - alpha) ** (measures - i)
        sum1 += weight * samples[i]
        sum2 += weight

    return sum1 / sum2


def calculate_macd(samples):
    return calculate_ema(samples, 12) - calculate_ema(samples, 26)


def calculate_signal(samples):
    sum1 = sum(samples[0:9])
    return sum1 / 9


def get_macds(samples):
    macds = [0 for i in range(26)]
    for i in range(26, len(samples)):
        macd = calculate_macd(samples[i - 26:i])
        macds.append(macd)

    return macds


def get_signals(macds):
    signals = []
    signals += macds[:9]

    for i in range(9, len(macds)):
        signal = calculate_signal(macds[i:])
        signals.append(signal)

    return signals

