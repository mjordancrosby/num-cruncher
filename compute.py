#!/usr/bin/env python

from decimal import getcontext, Decimal
import sys

MIN_VALUE = Decimal(0.0)
MAX_VALUE = Decimal(1000000000.0)

def compute_value(
        value: Decimal, 
        threshold: Decimal, 
        limit: Decimal, 
        total: Decimal,
    ) -> Decimal:
    """
    Compute value based on the provided threshold and limit.
    """

    if value < MIN_VALUE or value > MAX_VALUE:
        raise ValueError(f"Values must be between {MIN_VALUE:,.1f} and {MAX_VALUE:,.1f} inclusively")
    
    computed_value = Decimal()
    if value > threshold:
        computed_value = value - threshold

    if computed_value + total > limit:
        return limit - total
    
    return computed_value

def main():
    if len(sys.argv) != 3:
        print("Usage: python compute.py <threshold> <limit>", file=sys.stderr)
        sys.exit(1)
    
    try:
        threshold = Decimal(sys.argv[1])
    except Exception:
        print("threshold must be a numerical value", file=sys.stderr)
        sys.exit(1)

    if  not (MIN_VALUE <= threshold <= MAX_VALUE):
        print(f"threshold must be between {MIN_VALUE:,.1f} and {MAX_VALUE:,.1f} (inclusive)", file=sys.stderr)
        sys.exit(1)

    try:
        limit = Decimal(sys.argv[2])
    except Exception:
        print("limit must be a numerical value", file=sys.stderr)
        sys.exit(1)

    if  not (MIN_VALUE <= limit <= MAX_VALUE):
        print(f"limit must be between {MIN_VALUE:,.1f} and {MAX_VALUE:,.1f} (inclusive)", file=sys.stderr)
        sys.exit(1)


    total = Decimal(0.0)
    for line in sys.stdin:
        input_value = line.strip()
        if not input_value:
            continue

        try:
            value = Decimal(input_value)
            computed_value = compute_value(value, threshold, limit, total)
        except ValueError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
        except Exception:
            print(f"input value {line} not a numerical value", file=sys.stderr)
            sys.exit(1)

        total += computed_value
        print(f"{computed_value:.1f}")

    print(f"{total:.1f}")

if __name__ == "__main__":
    main()

