def orientation(p, q, r):
    val = (float(q[1]) - float(p[1])) * (float(r[0]) - float(q[0])) - (float(q[0]) - float(p[0])) * (float(r[1]) - float(q[1]))
    if abs(val) < 1e-3:
        return 0
    return 1 if val > 0 else 2

def on_segment(p, q, r):
    return (min(p[0], r[0]) - 1e-3 <= q[0] <= max(p[0], r[0]) + 1e-3 and
            min(p[1], r[1]) - 1e-3 <= q[1] <= max(p[1], r[1]) + 1e-3)

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True
    return False

def can_eliminate_all(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        segs = []
        for _ in range(n):
            parts = f.readline().strip().split()
            bx, by, gx, gy = float(parts[1]), float(parts[2]), float(parts[4]), float(parts[5])
            segs.append(((bx, by), (gx, gy)))

    for i in range(n):
        for j in range(i + 1, n):
            if do_intersect(segs[i][0], segs[i][1], segs[j][0], segs[j][1]):
                return "All Ghosts: were not eliminated"
    return "All Ghosts: eliminated"

import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(can_eliminate_all(sys.argv[1]))
    else:
        for i in range(9):
            print(f"ghostbusters_input_{i}.txt -> {can_eliminate_all(f'ghostbusters_input_{i}.txt')}")
