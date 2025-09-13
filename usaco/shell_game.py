# https://usaco.org/index.php?page=viewproblem2&cpid=891

n = int(input(""))  # No of inputs

swaps = []
guesses = []

for _ in range(n):
    g = input().strip().split(" ")
    swaps.append([int(i) for i in g[:2]])

    guesses.append(int(g[-1]))

h_score = 0

for init_pos in range(1, 4):
    pos = init_pos
    score = 0
    
    for swap, guess in zip(swaps, guesses):
        if pos == swap[0]:
            pos = swap[1]
        elif pos == swap[1]:
            pos = swap[0]

        if pos == guess:
            score += 1

    if score > h_score:
        h_score = score

print(h_score)
