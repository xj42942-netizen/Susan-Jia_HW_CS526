CS526 Homework 3

------------------------------------------------------------------------
Problem 1

Purpose:
This program determines whether each string in an input file is a palindrome and outputs the total number of palindromes found in the file.

Files Included:
Problem1_XJ.py
run_all_palindrome.sh

How to Run:
1. To test a single input file: python3 Problem1_XJ.py palindrome_0.txt
2. To automatically test all files: bash run_all_palindrome.sh

Output Format:
Each output file contains:
1. One line per string: "true" or "false"
2. The last line shows the total number of palindromes

Example:
Input file (palindrome_0.txt):

Command:
python3 Problem1_XJ.py palendrome_0.txt

Output:
False
True
False
True
False
True
3

------------------------------------------------------------------------
Problem 2

This program prints and counts all unique substrings of a given string using recursion.

Input: abcab
Output: bca, bc, abc, cab, c, b, a, abca, ca, ab, abcab, bcab -> 12

How to run:
python3 Problem2_XJ.py

------------------------------------------------------------------------
Problem 3
This program includes three recursive functions:
1. Reverse a stack implemented as an array
2. Reverse a stack implemented as a linked list
3. Reverse a stack implemented as a doubly linked list

------------------------------------------------------------------------
Problem 4
Purpose:
This program determines whether all Ghostbusters can eliminate ghosts without crossing beams. If any two beams intersect, not all ghosts can be eliminated.

How to Run:
python3 Problem4_XJ.py

Output Format:
The program prints results for all test files:
ghostbusters_input_0.txt -> All Ghosts: were not eliminated

