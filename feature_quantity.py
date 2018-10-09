import numpy as np
# 平均
def calc_mean(data):
    mean = sum(data) / len(data)
    return mean

# 移動平均(moving average)
def calc_maverage(data):
    # データ5つごとの移動平均
    a = np.ones(5)/5.0
    maverage = np.convolve(data, a, mode='same')
    return maverage

# 中央値
def calc_median(data):
    data.sort()
    num = len(data)
    if num % 2 == 0:
        median1 = num/2
        median2 = num/2 + 1
        median1 = int(median1)-1
        median2 = int(median2)-1
        median = (data[median1] + data[median2]) / 2
    else:
        median = (num + 1) / 2
        median = int(median) - 1
        median = data[median]
    return median

# 分散
def calc_variance(data):
    mean = calc_mean(data)
    diff = []

    for num in data:
        diff.append((num - mean)**2)

    sum_diff = sum(diff)
    variance = sum_diff / len(data)
    return variance

