import numpy as np


# Mean, Median, Max, Min, Range
def sub_task_1(n, size, inp):
    print("mean: ", np.mean(inp))
    print("median: ", np.median(inp))
    if n > 1:
        print("mean by column: ", np.mean(inp, axis=0))
        print("mean by row: ", np.mean(inp, axis=1))
        print("median by column: ", np.median(inp, axis=0))
        print("median by row: ", np.median(inp, axis=1))


# Variance & Standard Deviation
def sub_task_2(n, size, inp):
    pass


# Correlation, etc
def sub_task_3(n, size, inp):
    pass


def main():
    n: int = int(input("number of samples: "))
    size: int = int(input("sample size: "))
    inp = [
        [int(input("inp[{}][{}]: ".format(i, j))) for j in range(size)]
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
