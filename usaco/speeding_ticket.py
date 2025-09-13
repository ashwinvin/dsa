# https://usaco.org/index.php?page=viewproblem2&cpid=568
legal = []
bessie = []

val_split = lambda g: [int(v) for v in g.strip().split(" ")]

with open("inputs/speeding_ticket.txt") as file:
    contents = file.read().splitlines()
    n, m = val_split(contents[0])

    for i, line in enumerate(contents[1:]):
        length, speed = val_split(line)
        for _ in range(length):
            if i < n:
                legal.append(speed)
            else:
                bessie.append(speed)

speed_ticket = 0

for spd_lim, bes_spd in zip(legal, bessie):
    speed_ticket = max(speed_ticket, bes_spd - spd_lim)

print(speed_ticket)
