# Problem2_SJ.py

import os

# ---------- Load Input ----------
def load_input(filename):
    with open(filename, "r") as f:
        return list(map(int, f.read().split()))

# ---------- Radix Sort ----------
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Convert to prefix sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

def radix_sort(arr):
    if len(arr) == 0:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

# ---------- Run Radix Sort for One File & Save ----------
def process_one_file(input_file, output_file):

    arr = load_input(input_file)
    sorted_arr = radix_sort(arr[:])

    # Print to terminal
    print("\n====================================")
    print(f"Processing file: {input_file}")
    print("\nInput values:")
    print(arr)
    print("\nRadix Sort Result:")
    print(sorted_arr)

    # Save to output file
    with open(output_file, "w") as f:
        f.write(f"Processing file: {input_file}\n\n")
        f.write("Input values:\n")
        f.write(str(arr) + "\n\n")
        f.write("Radix Sort Result:\n")
        f.write(str(sorted_arr) + "\n")

    print(f"\nOutput saved to: {output_file}")

# ---------- Main ----------
def main():

    tasks = [
        ("input_small.txt",  "small_radix_output.txt"),
        ("input_medium.txt", "medium_radix_output.txt"),
        ("input_large.txt",  "large_radix_output.txt")
    ]

    for (inp, outp) in tasks:
        if os.path.exists(inp):
            process_one_file(inp, outp)
        else:
            print(f"\nError: {inp} not found.\n")

if __name__ == "__main__":
    main()
