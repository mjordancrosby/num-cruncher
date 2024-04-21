#! /bin/bash

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