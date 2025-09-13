from dataclasses import dataclass

TURNS = 100
CONTAINER_COUNT = 3


@dataclass
class MilkContainer:
    capacity: int
    reserve: int  # Amount of milk in container


containers: list[MilkContainer] = []

with open("inputs/milk_mixing.txt") as file:
    for line in file.readlines():
        vals = [int(val) for val in line.strip().split(" ")]
        containers.append(MilkContainer(capacity=vals[0], reserve=vals[1]))

cur_container = 0
for i in range(TURNS):
    buk1 = i % CONTAINER_COUNT
    buk2 = (i + 1) % CONTAINER_COUNT
    
    amnt_to_filled = min(
        containers[buk1].reserve, containers[buk2].capacity - containers[buk2].reserve
    )

    containers[buk2].reserve += amnt_to_filled
    containers[buk1].reserve -= amnt_to_filled

for container in containers:
    print(container.reserve)
