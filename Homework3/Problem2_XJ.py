# Problem 2: Using Recursion

def substrings_recursive(s, start, result):
    """Find all substrings using recursion."""

    if start == len(s):
        return
    
    for end in range(start + 1, len(s) + 1):
        substring = s[start:end]
        result.add(substring)
    
    substrings_recursive(s, start + 1, result)


def unique_substrings(s):
    """Find and print all unique substrings."""
    result = set()
    substrings_recursive(s, 0, result)

    # Print all sort
    print(", ".join(result), "->", len(result))
    sorted_result = sorted(result)


# main
if __name__ == "__main__":
    input_string = "abcab"
    print("Input:", input_string)
    unique_substrings(input_string)
