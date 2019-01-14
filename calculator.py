"""Simple calculator example for the practice of collaboration."""


class Calculator(object):
    """Simple calculator which has 4 functionalities.

    => add, sub, mul, div

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
            float: The quotient fo two given numbers.
        """
        return a / b

    def add(self, x, y):
        """Return the sum of two inputs.

        Given two numbers of float type x, y
        returns float type x + y

        Arg:
            x (float) : The first element of sum.
            y (float) : The second element of sum.

        Return:
            float : The sum of two given numbers.
        """
        return x + y
