#!/bin/bash

test_dir=$(dirname "$0")
source ${test_dir}/../test_utils.sh

test_happy_path() {
  echo "Running happy path test"
  expected=("4.5" "5.5" "10.0")
  input=("5.5" "9")
  actual=($(printf '%s\n' "${input[@]}" | docker run -i --rm solution:latest compute 1 10))
  check_output "${expected[*]}" "${actual[*]}"
  echo "Test passed"
}

test_non_root_user() {
  echo "Running test to check if the container runs as a non-root user"
  expected="compute"
  actual=$(docker run -i --rm solution:latest whoami)
  check_output "${expected}" "${actual}"
  echo "Test passed"
}

test_happy_path

test_non_root_user