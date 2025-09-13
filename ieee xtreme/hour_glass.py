#!/bin/python3
import os

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # i rows, j cols
    i = j = 0
    max_sum = 0
    get_row_sub_sum = lambda n, sarr: sum([sarr[n + k] for k in range(3)])
    while i <= (6 - 3):
        while j <= (6 - 3):
            curr_sum = (
                get_row_sub_sum(j, arr[i])
                + get_row_sub_sum(j, arr[i + 2])
                + arr[i + 1][j + 1]
            )
            if i == 0 and j == 0:
                max_sum = curr_sum

            max_sum = max(max_sum, curr_sum)
            j += 1
        i += 1
        j = 0
    return max_sum


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


    result = hourglassSum(arr)

    fptr.write(str(result) + "\n")

    fptr.flush()
