import os

# ---------- Load Input ----------
def load_input(filename):
    with open(filename, "r") as f:
        return list(map(int, f.read().split()))

# ---------- Merge Sort ----------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    return res + left[i:] + right[j:]

# ---------- Quick Sort ----------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# ---------- Insertion Sort ----------
def insertion_sort(arr):
    arr = arr[:]  # copy
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# ---------- Run Sorting for One File & Save ----------
def process_one_file(input_file, output_file):

    arr = load_input(input_file)

    merge_result = merge_sort(arr[:])
    quick_result = quick_sort(arr[:])
    insertion_result = insertion_sort(arr[:])

    # print to screen
    print("\n====================================")
    print(f"Processing file: {input_file}")
    print("\nInput values:")
    print(arr)
    print("\nMerge Sort:")
    print(merge_result)
    print("\nQuick Sort:")
    print(quick_result)
    print("\nInsertion Sort:")
    print(insertion_result)

    # save to file
    with open(output_file, "w") as f:
        f.write(f"Processing file: {input_file}\n\n")
        f.write("Input values:\n")
        f.write(str(arr) + "\n\n")
        f.write("Merge Sort:\n")
        f.write(str(merge_result) + "\n\n")
        f.write("Quick Sort:\n")
        f.write(str(quick_result) + "\n\n")
        f.write("Insertion Sort:\n")
        f.write(str(insertion_result) + "\n")

    print(f"\nOutput saved to: {output_file}")

# ---------- Main ----------
def main():

    tasks = [
        ("input_small.txt",  "problem1_small_output.txt"),
        ("input_medium.txt", "problem1_medium_output.txt"),
        ("input_large.txt",  "problem1_large_output.txt"),
    ]

    for (inp, outp) in tasks:
        if os.path.exists(inp):
            process_one_file(inp, outp)
        else:
            print(f"\nMissing file: {inp}")

if __name__ == "__main__":
    main()
