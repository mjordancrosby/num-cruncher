from decimal import Decimal
import unittest

from lib import compute_value, check_bounds

class TestComputeValue(unittest.TestCase):
    """
    Test the compute_value function in compute.py
    """

    def test_over_threshold(self):
        """
        The computed value should be the difference between value and threshold 
        when the value is greater than the threshold.
        """
        computed_value = compute_value(Decimal('10'), Decimal('6'), Decimal('20'), Decimal('0'))
        self.assertEqual(computed_value, Decimal(4.0))
    
    def test_under_threshold(self):
        """
        The computed value should be 0
        when the value is less than the threshold.
        """
        computed_value = compute_value(Decimal('10'), Decimal('11'), Decimal('20'), Decimal('0'))
        self.assertEqual(computed_value, Decimal())

    def test_equal_to_threshold(self):
        """
        The computed value should be 0
        when the value is equal to the threshold.
        """
        computed_value = compute_value(Decimal('10'), Decimal('10'), Decimal('20'), Decimal('0'))
        self.assertEqual(computed_value, Decimal())
    
    def test_computed_exceeds_limit(self):
        """
        The next computed value cannot exceed the limit.
        """
        computed_value = compute_value(Decimal('10'), Decimal('4'), Decimal('5'), total=Decimal('2'))
        self.assertEqual(computed_value, Decimal('3'))

    def test_computed_limit_exceeded(self):
        """
        The next computed value is 0 when the total computed values already exceeds the limit.
        """
        computed_value = compute_value(Decimal('10'), Decimal('4'), Decimal('5'), total=Decimal('5'))
        self.assertEqual(computed_value, Decimal('0'))

    def test_fix_point_precision(self):
        """
        The computed value calculation should use the fixed point arithmatic 
        and exact representation of decimal value. i.e 3.3 - 1.1 != 2.1999999999999997
        """
        computed_value = compute_value(Decimal('3.3'), Decimal('1.1'), Decimal('5'), Decimal('0'))
        self.assertEqual(computed_value, Decimal('2.2'))

    def test_precision_to_tenths_places(self):
        """
        The computed value calculation is accurate to tenths places.
        """
        computed_value = compute_value(Decimal('1000000000'), Decimal('0.1'), Decimal('1000000000'), Decimal('0'))
        self.assertEqual(computed_value, Decimal('999999999.9'))

class TestBoundsCheck(unittest.TestCase):
    """
    Test the MIN_VALUE and MAX_VALUE bounds.
    """

    def test_min_value(self):
        """
        Lower bounds is accepted.
        """
        try:
            check_bounds(Decimal('0.0'))
        except ValueError:
            self.fail("check_bounds() raised ValueError unexpectedly!")

    def test_max_value(self):
        """
        Upper bounds is accepted.
        """
        try:
            check_bounds(Decimal('1000000000.0'))
        except ValueError:
            self.fail("check_bounds() raised ValueError unexpectedly!")

    def test_value_below_min_value(self):
        """
        Error raised for values below the minimum value.
        """
        with self.assertRaises(ValueError) as context:
            check_bounds(Decimal('-1'))

        self.assertEqual('Must be between 0.0 and 1,000,000,000.0 (inclusive)', str(context.exception))

    def test_value_above_max_value(self):
        """
        Error raised for values above the maximum value.
        """
        with self.assertRaises(ValueError) as context:
            check_bounds(Decimal('1000000000.1'))

        self.assertEqual('Must be between 0.0 and 1,000,000,000.0 (inclusive)', str(context.exception))

if __name__ == '__main__':
    unittest.main()