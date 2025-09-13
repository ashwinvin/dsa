# https://usaco.org/index.php?page=viewproblem2&cpid=665

val_split = lambda g: [int(v) for v in g.strip().split(" ")]

lines = []
m = n = k = 0

with open("inputs/cow_signal.txt") as file:
    contents = file.read().splitlines()
    m, n, k = val_split(contents[0])
    lines = [line for line in contents[1:]]

amplified_lines = []

for line in lines:
    amp_str = ""
    for char in line:
        amp_str += char * k
    for _ in range(k):
        amplified_lines.append(amp_str)

for line in amplified_lines:
    print(line)
