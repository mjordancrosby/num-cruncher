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
    
    getcontext().prec = 20
    computed_value = Decimal()
    if value > threshold:
        computed_value = value - threshold

    if computed_value + total > limit:
        return limit - total
    
    return computed_value

def format_decimal(value: Decimal) -> str:
    """
    Format decimal value to string with 10 decimal places.
    """
    if value.as_tuple().exponent == 0:
        return f"{value:.1f}"
    return str(value)


def main():
    getcontext().prec = 10


    threshold = Decimal(sys.argv[1])
    limit = Decimal(sys.argv[2])

    total = Decimal(0.0)
    for line in sys.stdin:
        try:
            value = Decimal(line.strip())
        except ValueError:
            print("Input must be numerical values")
            sys.exit(1)

        computed_value = compute_value(value, threshold, limit, total)
        total += computed_value
        print(format_decimal(computed_value))

    print(format_decimal(total))

if __name__ == "__main__":
    main()

