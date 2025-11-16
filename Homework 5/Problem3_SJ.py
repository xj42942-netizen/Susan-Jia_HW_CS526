import os
from math import inf

BASE = r"/Users/xibeijia/Desktop/25 fall 526/cs 526 HW5"
FILES = [f"longest_seq{i}.txt" for i in range(1, 7)]
def readfile(filename):
    path = os.path.join(BASE, filename)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    A = list(map(int, lines[2].strip().split()))
    B = list(map(int, lines[3].strip().split()))
    return A, B

def longest_seq(A, B):
    m, n = len(A), len(B)
    memo = {}

    # prev_position: index in the "previous" array depending on turn; -1 means empty
    # cur_turn: "A" or "B"
    def set_position(prev_position, cur_turn):
        key = (prev_position, cur_turn)
        if key in memo:
            return memo[key]

        if cur_turn == "A":
            prev_value = -inf if prev_position == -1 else B[prev_position]
            max_len = 0
            for i in range(prev_position + 1, m):
                if A[i] > prev_value:
                    num = 1 + set_position(i, "B")
                    if num > max_len:
                        max_len = num
        else:
            prev_value = -inf if prev_position == -1 else A[prev_position]
            max_len = 0
            for j in range(prev_position + 1, n):
                if B[j] > prev_value:
                    num = 1 + set_position(j, "A")
                    if num > max_len:
                        max_len = num

        memo[key] = max_len
        return max_len

    return max(set_position(-1, "A"), set_position(-1, "B"))

if __name__ == "__main__":
    for fname in FILES:
        A, B = readfile(fname)
        ans = longest_seq(A, B)
        print(f"File Input: {fname}")
        print(f"Longest Sequence: {ans}\n")
