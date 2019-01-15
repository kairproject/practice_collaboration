"""Simple calculator example for the practice of collaboration."""


class Calculator(object):
    """Simple calculator which has 4 functionalities.

    => add, sub, mul, div
    => bitwise_shift_left, bitwise_shift_right, bitwise_and
    => bitwise_or, bitwise_not, bitwise_xor

    All methods will be implemented as staticmethods
    so that it can be called without making an object.

    !!Don't forget to run static analyzers and unittests
    before pushing your code. (check 100% test covered)
    """

    def div(self, a, b):
        """Return quotient of two given numbers.

        Given two numbers float type a, b
        returns float type a/b.

        Arg:
            a (float): The dividend of dvision function.
            b (float): The divisor of dvision function.

        Return:
            float: The quotient of two given numbers.
        """
        return a / b

    def sub(self, a: float, b: float) -> float:
        """Subtraction method for calculator class.

        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Args:
            a (float): The left operand of subtraction.
            b (float): The right operand of subtraction.
        Returns:
            Subtraction of a to b.

        """
        return a - b

    def bitwise_or(self, a: int, b: int) -> int:
        """Copy a bit if it exists in either operand.

        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Args:
            a (int): The left operand of bitwise or.
            b (int): The right operand of bitwise of.
        Returns:
            Bit which exists in either operand.

        """
        return a | b

    def bitwise_xor(self, a, b):
        """Return  xor of two given numbers.

        Given two numbers int type a, b
        returns int type a^b.

        Arg:
            a (int)
            b (int)

        Return:
            int: The xor result of two given numbers.
        """
        return a ^ b
