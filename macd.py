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


def analyze_macd(dates, macds, signals, values, funds):
    money = funds
    actions = 0
    for i in range(1, len(macds)):
        # signal cuts from below -> buy action
        if signals[i - 1] < macds[i - 1] and signals[i] > macds[i]:
            if money != 0:
                actions = money / values[i]
                money = 0
            print("Buy: " + dates[i])
            print("Actions: " + str(actions))
        # signal cuts from above -> sell actions
        if signals[i - 1] > macds[i - 1] and signals[i] < macds[i]:
            if actions != 0:
                money = actions * values[i]
                actions = 0
            print("Sell: " + dates[i])
            print("Money: " + str(money))

    print("\nFunds before period: " + str(funds))
    print("Funds after whole period: " + str(money))
    print("Funds after whole period after selling actions: " + str(actions * values[len(values) - 1]))

