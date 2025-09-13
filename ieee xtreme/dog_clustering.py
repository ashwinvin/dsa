# Topics - Difference lists, use of arithmetic tricks
def calc(n_group, weights):
    diff_list = [0] * (len(weights) - 1)
    i = 0

    while i < len(weights) - 1:
        diff_list[i] = weights[i + 1] - weights[i]
        i += 1
    diff_list = sorted(diff_list, reverse=True)

    spread_sum = (weights[-1] - weights[0]) - sum(diff_list[: n_group - 1]) 

    return spread_sum


print(calc(4, sorted([30,40,20,41,50])))
