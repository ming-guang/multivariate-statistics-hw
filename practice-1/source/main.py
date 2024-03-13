import numpy as np


def nanptp(inp, axis=None):
    if axis == 0:
        return [nanptp(np.array(inp[:, i])) for i in range(inp.shape[1])]
    if axis == 1:
        return [nanptp(np.array(row)) for row in inp]
    target = [[]]
    if len(inp.shape) > 1:
        target = [[x for x in row if not np.isnan(x)] for row in inp]
    else:
        target = [[x for x in inp if not np.isnan(x)]]
    min = np.inf
    max = -np.inf
    for row in target:
        for x in row:
            if x < min:
                min = x
            if x > max:
                max = x
    return max - min


# Mean, Median, Max, Min, Range
def sub_task_1(n, size, inp):
    print("mean: ", np.nanmean(inp))
    print("median: ", np.nanmedian(inp))
    print("range: ", nanptp(inp))
    if n > 1:
        print("mean by column: ", np.nanmean(inp, axis=0))
        print("mean by row: ", np.nanmean(inp, axis=1))
        print("median by column: ", np.nanmedian(inp, axis=0))
        print("median by row: ", np.nanmedian(inp, axis=1))
        print("range by row: ", nanptp(inp, axis=0))
        print("range by column: ", nanptp(inp, axis=1))


# Variance & Standard Deviation
def sub_task_2(n, size, inp):
    print("var: ", np.nanvar(inp))
    print("std: ", np.nanstd(inp))
    pass


# Correlation, etc
def sub_task_3(n, size, inp):
    pass


def float_or_nan(n):
    try:
        return float(n)
    except ValueError:
        return np.NaN


def main():
    n: int = int(input("number of samples: "))
    size: int = int(input("sample size: "))
    inp = [
        [float_or_nan(input("inp[{}][{}]: ".format(i, j))) for j in range(size)]
        for i in range(n)
    ]
    inp = np.array(inp)
    print("input array:")
    print(inp)
    sub_task_1(n, size, inp)
    sub_task_2(n, size, inp)
    sub_task_3(n, size, inp)


if __name__ == "__main__":
    main()
