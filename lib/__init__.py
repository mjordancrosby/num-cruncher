from decimal import Decimal

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
    
    computed_value = Decimal()
    if value > threshold:
        computed_value = value - threshold

    if computed_value + total > limit:
        return limit - total
    
    return computed_value

def check_bounds(value: Decimal):
    """
    Check if the value is within the bounds.
    """
    if value < MIN_VALUE or value > MAX_VALUE:
        raise ValueError(f"Must be between {MIN_VALUE:,.1f} and {MAX_VALUE:,.1f} (inclusive)")

