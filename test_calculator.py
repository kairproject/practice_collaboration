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
        """Check 3 test cases. Vary input signs and check the results.

        First unit test : check two positive inputs.
        Second unit test : check one negative input and one positive input.
        Third unit test : check two negative inputs.
        """
        cal = Calculator()
        assert cal.sub(10.0, 7.3) == 2.7
        assert cal.sub(-6.3, 7.3) == -13.6
        assert cal.sub(-2.0, -3.1) == 1.1

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

    def test_bitwise_or(self):
        """Put your test casese for bitwise_or  that starts with assert."""
        calc = Calculator()
        result = calc.bitwise_or(0b010000, 0b100000)
        assert result == 0b110000

        result = calc.bitwise_or(0b00011, 0b110000)
        assert result == 0b110011

        result = calc.bitwise_or(0b0010, 0b1000)
        assert result == 0b1010
