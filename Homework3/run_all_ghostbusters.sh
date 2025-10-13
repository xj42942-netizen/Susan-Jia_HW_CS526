#!/bin/bash
# Run all ghostbusters input files separately

for i in {0..8}
do
  echo "Running ghostbusters_input_${i}.txt ..."
  python3 Problem4_XJ.py ghostbusters_input_${i}.txt > ghostbusters_ans_${i}.txt
done

echo "✅ All tests completed."
