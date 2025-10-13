# Course: CS526 Homework 3

import sys

def is_palindrome(s):
    """Return True if string s is a palindrome."""
    return s.lower() == s.lower()[::-1]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Problem1_XJ.py <inputfile>")
        return

    input_file = sys.argv[1]
    palindrome_count = 0

    try:
        with open(input_file, 'r') as f:
            for line in f:
                word = line.strip()
                if word == "":
                    continue
                if is_palindrome(word):
                    print("true")
                    palindrome_count += 1
                else:
                    print("false")
        print(palindrome_count)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

if __name__ == "__main__":
    main()
