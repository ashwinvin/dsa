n_tests = int(input())


def calc(p, s, mem_locs):
    fifo = []
    lru = []
    counts = [0, 0]  # 0: fifo, 1: lru
    for addr in mem_locs:
        p_no = addr // s

        if p_no not in fifo:
            if len(fifo) == p:
                fifo.remove(fifo[0])
                counts[0] += 1
            fifo.append(p_no)

        if p_no not in lru and len(lru) == p:
            lru.pop()
            counts[1] += 1
        elif p_no in lru:
            lru.remove(p_no)

        lru.insert(0, p_no)
    return "yes" if counts[0] > counts[1] else "no", str(counts[0]), str(counts[1])


store = []  # (no of pages, size of each page, mem_locs)
for i in range(n_tests):
    p, s, n = [int(val) for val in input().split(" ")]
    mem_locs = []

    for _ in range(n):
        mem_locs.append(int(input()))
    store.append((p, s, mem_locs))

for p, s, mem_locs in store:
    res = calc(p, s, mem_locs)
    print(" ".join(res))
