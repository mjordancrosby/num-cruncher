from decimal import Decimal
import unittest

from compute import compute_value

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

    def test_precision_to_10_places(self):
        """
        The computed value calculation is accurate to 10 decimal places.
        """
        computed_value = compute_value(Decimal('1000000000'), Decimal('0.0000000001'), Decimal('1000000000'), Decimal('0'))
        self.assertEqual(computed_value, Decimal('999999999.9999999999'))

    def test_value_exceeds_max_value(self):
        """
        An exception should be raised when the value exceeds the maximum value.
        """

        with self.assertRaises(ValueError) as context:
            compute_value(Decimal('1000000000.1'), Decimal('1'), Decimal('1000000000'), Decimal('0'))

        self.assertEqual('Values must be between 0.0 and 1,000,000,000.0 inclusively', str(context.exception))

    def test_value_exceeds_min_value(self):
        """
        An exception should be raised when the value is below the minimum value.
        """

        with self.assertRaises(ValueError) as context:
            compute_value(Decimal('-1'), Decimal('1'), Decimal('1000000000'), Decimal('0'))

        self.assertEqual('Values must be between 0.0 and 1,000,000,000.0 inclusively', str(context.exception))



if __name__ == '__main__':
    unittest.main()