#!/bin/bash
test_dir=$(dirname "$0")

fail_test() {
  expected=$1
  actual=$2
  echo "Test failed"
  echo "Actual output did not match expected output"
  echo "Expected: ${expected}"
  echo "Actual: ${actual}"
  exit 1
}

check_output() {
  expected=($1)
  actual=($2)
  if [ "${#expected[@]}" -ne "${#actual[@]}" ]; then
      fail_test "${expected[*]}" "${actual[*]}"
  fi

  for i in "${!expected[@]}"; do
      if [ "${expected[i]}" != "${actual[i]}" ]; then
        fail_test "${expected[*]}" "${actual[*]}"
      fi
  done
}

test_happy_path() {
  echo "Running happy path test"
  expected=("0.0" "0.0" "0.0" "1.5" "19000.0" "19980998.5" "20000000.0")
  actual=($(cat $test_dir/input | python3 $test_dir/../../compute.py 1000 20000000))
  check_output "${expected[*]}" "${actual[*]}"
  echo "Test passed"
}

test_zero_threshold() {
  echo "Running test for zero threshold"
  expected=("19.0" "0.0" "1000.0" "1001.5" "20000.0" "19977979.5" "20000000.0")
  actual=($(cat $test_dir/input | python3 $test_dir/../../compute.py 0 20000000))
  check_output "${expected[*]}" "${actual[*]}"
  echo "Test passed"
}

test_zero_limit() {
  echo "Running test for zero threshold"
  expected=("0.0" "0.0" "0.0" "0.0" "0.0" "0.0" "0.0")
  actual=($(cat $test_dir/input | python3 $test_dir/../../compute.py 1000 0))
  check_output "${expected[*]}" "${actual[*]}"
  echo "Test passed"
}

test_no_input() {
  echo "Running test for no input"
  expected="0.0"
  actual=$(echo "" | python3 $test_dir/../../compute.py 1.1 1.1)
  check_output "${expected}" "${actual}"
  echo "Test passed"
}

assert_error() {
  if [ $? -eq 0 ]; then
    echo "Test failed. Expected error"
    exit 1
  fi

  expected=$1
  actual=$2

  if [ "$expected" != "$actual" ]; then
    fail_test "${expected}" "${actual}"
  fi
}

test_required_args() {
  echo "Running test for missing required arguments"
  expected="Usage: python compute.py <threshold> <limit>"
  actual=$(python3 $test_dir/../../compute.py 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"
}

test_threshold_below_min() {
  echo "Running test for threshold below minimum"
  expected="threshold must be between 0.0 and 1,000,000,000.0 (inclusive)"
  actual=$(python3 $test_dir/../../compute.py -1 1000 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"
}

test_threshold_above_max() {
  echo "Running test for threshold above maximum"
  expected="threshold must be between 0.0 and 1,000,000,000.0 (inclusive)"
  actual=$(python3 $test_dir/../../compute.py 1000000001 1000 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"
}

test_threshold_not_a_number() {
  echo "Running test for threshold not a number"
  expected="threshold must be a numerical value"
  actual=$(python3 $test_dir/../../compute.py abc 1000 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"
}

test_limit_below_min() {
  echo "Running test for limit below minimum"
  expected="limit must be between 0.0 and 1,000,000,000.0 (inclusive)"
  actual=$(python3 $test_dir/../../compute.py 1000 -1 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"
}

test_limit_above_max() {
  echo "Running test for limit above maximum"
  expected="limit must be between 0.0 and 1,000,000,000.0 (inclusive)"
  actual=$(python3 $test_dir/../../compute.py 1000 1000000001 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"
}

test_limit_not_a_number() {
  echo "Running test for limit not a number"
  expected="limit must be a numerical value"
  actual=$(python3 $test_dir/../../compute.py 1000 abc 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"
}

test_input_value_not_a_number() {
  echo "Running test for input value not a number"
  expected="input value abc not a numerical value"
  actual=$(cat $test_dir/not_a_number_input | python3 $test_dir/../../compute.py 1000 1000 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"
}

test_input_value_above_max() {
  echo "Running test for input value above maximum"
  expected="Values must be between 0.0 and 1,000,000,000.0 inclusively"
  actual=$(cat $test_dir/above_max_input | python3 $test_dir/../../compute.py 1000 1000 2>&1 > /dev/null)
  assert_error "$expected" "$actual"
  echo "Test passed"

}

echo "Running e2e tests"

test_happy_path

test_zero_threshold

test_zero_limit

test_no_input

test_required_args

test_threshold_below_min

test_threshold_above_max

test_threshold_not_a_number

test_limit_below_min

test_limit_above_max

test_limit_not_a_number

test_input_value_not_a_number

test_input_value_above_max