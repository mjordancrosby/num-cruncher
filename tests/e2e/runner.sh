#!/bin/bash
test_dir=$(dirname "$0")

test_happy_path() {
  expected=("0.0" "0.0" "0.0" "1.5" "19000.0" "19980998.5" "20000000.0")
  actual=($(cat $test_dir/input | python3 $test_dir/../../compute.py 1000 20000000))

  echo "Running happy path test"
    if [ "${#expected[@]}" -ne "${#actual[@]}" ]; then
      echo "Actual output did not match expected output"
      echo "Expected: ${expected[*]}"
      echo "Actual: ${actual[*]}"
      exit 1
  fi

  for i in "${!expected[@]}"; do
      if [ "${expected[i]}" != "${actual[i]}" ]; then
        echo "Actual output did not match expected output"
        echo "Expected: ${expected[*]}"
        echo "Actual: ${actual[*]}"
        exit 1
      fi
  done
  echo "Test passed"
}

echo "Running e2e tests"

test_happy_path