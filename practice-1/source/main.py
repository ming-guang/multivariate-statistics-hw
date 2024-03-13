import numpy as np


# Mean, Median, Max, Min, Range
def sub_task_1(n, size, inp):
    print("mean: ", np.nanmean(inp))
    print("median: ", np.nanmedian(inp))
    if n > 1:
        print("mean by column: ", np.nanmean(inp, axis=0))
        print("mean by row: ", np.nanmean(inp, axis=1))
        print("median by column: ", np.nanmedian(inp, axis=0))
        print("median by row: ", np.nanmedian(inp, axis=1))


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
