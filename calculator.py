"""Simple calculator example for the practice of collaboration."""
# -*- coding: utf-8 -*-
"""
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * validate the code

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

class Calculator(object):
    """Simple calculator which has 4 functionalities.

    => add, sub, mul, div

    All methods will be implemented as staticmethods
    so that it can be called without making an object.

    !!Don't forget to run static analyzers and unittests
    before pushing your code. (check 100% test covered)
    """
    def init(self):
        return

    def mul(sef, a: float, b: float)->float:
        c = a*b
        return c

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
