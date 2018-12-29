"""Test cases for calculator.py."""

from calculator import Calculator


class TestCalculator():
    """This class has 4 methods to test add, sub, mul, and div respectively.

    Note that the test class doesn't have a constructor.

    !!Don't forget to check all implementation covered by tests.
    """

    def test_add(self):
        """Put your test cases for add that starts with assert."""
        pass

    def test_sub(self):
        """Put your test cases for sub that starts with assert."""
        assert Calculator.sub(10.0, 7.3) == 2.7
        assert Calculator.sub(6.3, 7.3) == -1.0
        assert Calculator.sub(2.0, 3.1) == -1.1

    def test_mul(self):
        """Put your test cases for mul that starts with assert."""
        pass

    def test_div(self):
        """Put your test cases for div that starts with assert."""
        pass
