# def get_vals() -> list[int]:
#     vals = [el for el in input().split(" ")]
#     return [int(el) for el in vals]


# n_el, n_rot = get_vals()
# arr = [el for el in get_vals()]
n_rot = 4
arr = [
    1,
    2,
    3,
    4,
    5,
]


def rotate_arr(arr, d):
    h_map = {}

    for i, el in enumerate(arr):
        new_pos = i - d
        if new_pos < 0:
            new_pos = len(arr) + new_pos 
        h_map[new_pos] = el

    for i, el in h_map.items():
        arr[i] = el

    return arr


arr = rotate_arr(arr, n_rot)
print(arr)
