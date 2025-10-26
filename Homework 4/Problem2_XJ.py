import os

def compute_min_elements(filename):
    """Compute smallest number of elements whose sum > target T"""
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        T = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    arr.sort(reverse=True)

    sum_val = 0
    count = 0
    for num in arr:
        sum_val += num
        count += 1
        if sum_val > T:
            break

    return count


# === process fewest_1, fewest_2, fewest_3 ===
results = []
for i in range(1, 4):
    fname = f"fewest_{i}.txt"
    if os.path.exists(fname):
        answer = compute_min_elements(fname)
        results.append(f"answer{i}: {answer}")
        print(f"{fname} -> answer{i}: {answer}")
    else:
        print(f"{fname} not found, skipping.")

# ==== Save to answers_fewest.txt ====
with open("answers_fewest.txt", "w") as f:
    f.write("\n".join(results) + "\n")
