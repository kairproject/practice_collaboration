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
        pass

    def test_mul(self):
        """Put your test cases for mul that starts with assert."""
        pass

    def test_div(self):
        """Put your test cases for div that starts with assert."""
        calc = Calculator()
        result = calc.div(4.2, 2.1)
        assert result == 2

        result = calc.div(5, 2.)
        assert result == 2.5

        result = calc.div(100, 20.)
        assert result == 5

        result = calc.div(5.e10, 10.)
        assert result == 5.e9

        result = calc.div(1., 1.e5)
        assert result == 1.e-5

    def test_bitwise_not(self):
        """Put your test cases for bitwise not that starts with assert.

        To use:
        calc = Calculator()
        result = calc.bitwise_not(60)
        assert result == -61
        """
        calc = Calculator()
        result = calc.bitwise_not(60)
        assert result == -61

        result = calc.bitwise_not(5)
        assert result == -6

        result = calc.bitwise_not(84)
        assert result == -85
