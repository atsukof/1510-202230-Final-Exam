"""
(3 points) Implement an annotated recursive function called sum_of_digits that accepts a positive
           integer and returns the sum of the digits in the integer.

           For example:

           sum_of_digits(123) will return 6 (not "6" which is a string) because 1 + 2 + 3 = 6

(1 point) If this function is passed a negative integer, it must raise a ValueException.

(1 point) This function needs a docstring that includes 2 useful doctests.

(1 point) Prove this function correctly raises a ValueException when passed a negative inside the
        main function. Do not let the program crash!
"""


def sum_of_digits(positive_integer: int) -> int:
    """
    Calculate the sum of the digits in the integer.

    :param positive_integer: a positive integer
    :precondition: positive_integer must be a positive integer
    :postcondition: calculates the sum of the digits in the integer
    :return: the sum of the digits in the integer

    >>> sum_of_digits(156)
    12

    >>> sum_of_digits(-20)
    You entered a non-positive integer.
    """
    try:
        if positive_integer < 0:
            raise ValueError
    except ValueError:
        print("You entered a non-positive integer.")
    except TypeError:
        print("You entered a non-number value.")
    else:
        integer_string = str(positive_integer)
        sum_digit = int(integer_string[0])
        if len(integer_string) > 1:
            sum_digit += sum_of_digits(int(integer_string[1:]))
        return sum_digit


def main():
    """
    Drive the program.
    """
    my_integer = 123
    sum_of_digits(my_integer)
    print(sum_of_digits(my_integer))

    your_integer = -10
    print(sum_of_digits(your_integer))


if __name__ == "__main__":
    main()
