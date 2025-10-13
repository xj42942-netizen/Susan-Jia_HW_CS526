#!/bin/bash
# Run palindrome tests for files 0–4 and their L/S variants

for i in {0..4}
do
  for t in "" "L" "S"
  do
    input="palendrome_${i}${t}.txt"
    output="palendrome_ans_${i}${t}.txt"

    if [ -f "$input" ]; then
      echo "Running test: $input"
      python3 Problem1_XJ.py "$input" > "$output"
    fi
  done
done
