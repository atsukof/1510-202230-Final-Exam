"""

FUNCTION:
_________

Define a function called denomination_registrar.

This function accepts a non-empty sorted tuple of ints and floats called denominations.

This function uses this sorted tuple when it customizes and returns an inner function called change_maker.

The change_maker function is used to make change rounded to the closest 20th of a unit. It does this
using the algorithm you implemented for money_changer in A2. Yes, you may use code you wrote for A2 here.

Sample usage example 1 to go in your main function:

canadian_denominations = (100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05)
canadian_change_maker = denomination_registrar(canadian_denominations)
canadian_breakdown = canadian_change_maker(66.53)
print(canadian_breakdown)
[0, 1, 0, 1, 1, 0, 1, 2, 0, 1] # expected output

Sample usage example 2 to go in your main function:

euro_denominations = (500, 200, 100, 50, 20, 10, 5, 2, 1, .50, .20, .10, .05)
euro_change_maker = denomination_registrar(euro_denominations)
euro_breakdown = euro_change_maker(870.53)
print(euro_breakdown)
[1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1] # expected output

ASSUMPTIONS (PRECONDITIONS):
____________

Currencies in the tuple are pre-sorted with the highest value at index 0.

The smallest currency you need to worry about is worth 1/20th  of a unit, i.e., 0.05. Don't worry about anything
smaller.

The denomination_registrar function accepts a tuple and returns a change_maker function that uses the tuple.

The change_maker function accepts a float representing some money and returns a list.

Since the smallest denomination we use is 0.05, the floats will never have more than 2 digits after the decimal.

Your change_maker function must round to the closest 0.05.

The list change_maker returns has the same length as the tuple passed to denomination_registrar, of course

DOCSTRING:
__________

No. No docstrings are needed.

DOCTESTS:
_________

No. No doctests are needed.

UNIT TESTS:
___________

No. No unit tests are needed.

MAIN FUNCTION AND IF-STATEMENT BELOW IT
_______________________________________

Yes. The main function should contain the code in the examples to demo your code.

"""
