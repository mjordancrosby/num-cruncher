# Overview

Given the `n` inputs, outputs `1..n` will be produced based on these values,
taking into account the `threshold` and `limit` arguments.

The `threshold` argument will be used to modify every input so that if the input
amount is greater than the threshold, the output amount will be the portion of
the input value that exceeds the threshold. If the input is less than the
threshold, the output should be zero. Put another way, the output value
will be the larger of 0.0 or the value of `[input] - [threshold]`.

The `limit` amount serves to further constrain the output values. The cumulative
sum of of all `n` outputs must never exceed this value, however the individual
output values must be maximized in the order they are given without breaking the
rules imposed by `threshold` and `limit`.

After all inputs are processed, output value `n+1` will be written. It must be
equal to the sum of all `n` output values. It follows from the rules above that
output `n+1` must always be less than or equal to the `limit` argument
specified.b

## Usage

To use test the solution run the following docker commands:

1. `docker build -t solution .`
2. `cat input | docker run -i --rm solution:latest compute 100 5000`

### Make Commands

|   Target |                                Description |
| -------: | -----------------------------------------: |
| unittest |                             Run unit tests |
|      e2e |                              Run e2e tests |
|    tests |                Run both unit and e2e tests |
|    build |                         Build docker image |
|      all | Run tests and build image (default target) |
