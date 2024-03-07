def calculate_ema(samples, measures):
    samples_number = len(samples)
    alpha = 2 / (samples_number - 1)
    samples = samples[measures:]

    sum1 = 0
    sum2 = 0
    for i in range(measures, 0, 1):
        weight = (1 - alpha) ** (samples_number - measures - 1)
        sum1 += weight * samples[i]
        sum2 += weight

    return sum1 / sum2
