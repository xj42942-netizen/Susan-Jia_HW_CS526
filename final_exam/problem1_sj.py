import sys
import heapq


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    n = int(next(it))
    threshold = int(next(it))
    drain = int(next(it))

    cracks = []
    for _ in range(n):
        a = int(next(it))
        s = int(next(it))
        cracks.append((a, s))

    heap = []
    idx = 0
    t = cracks[0][0] if n > 0 else 0

    water = 0
    max_water = 0
    sum_sizes = 0
    cnt = 0

    while True:
        if cnt == 0 and idx >= n:
            break

        if cnt == 0 and idx < n and t < cracks[idx][0]:
            gap = cracks[idx][0] - t
            water = max(0, water - gap * drain)
            t = cracks[idx][0]

        while idx < n and cracks[idx][0] == t:
            a, s = cracks[idx]
            key = s - a
            heapq.heappush(heap, -key)
            sum_sizes += key + t
            cnt += 1
            idx += 1

        if cnt > 0:
            key = -heapq.heappop(heap)
            sum_sizes -= key + t
            cnt -= 1

        water = max(0, water + sum_sizes - drain)
        max_water = max(max_water, water)

        if water >= threshold:
            print("FLOOD")
            print(t)
            print(water)
            return

        sum_sizes += cnt
        t += 1

    print("SAFE")
    print(max_water)


if __name__ == "__main__":
    main()
