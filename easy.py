"""

FUNCTION:
_________

Define a function called merge(first, second). This function accepts two sorted lists called
first and second and returns a new sorted list that contains the elements from first and second.

ASSUMPTIONS (PRECONDITIONS):
____________

The lists passed as parameters, first and second, may not be modified, not even temporarily.
The lists passed as parameters must be pre-sorted.
The lists will always be homogenous and the same types, so they are sortable and can be merged.
The lists can be strings or some other sortable like numbers.

Sample usage example 1:

some_list = [1, 5, 9]
some_other_list = [-10, 44, 100]
sorted_merge = merge(some_list, some_other_list)
print(sorted_merge)
[-10, 1, 5, 9, 44, 100]

Sample usage example 2:

some_list = ["apple", "orange", "tamarind"]
some_other_list = ["applesauce", "bread", "watermelon"]
sorted_merge = merge(some_list, some_other_list)
print(sorted_merge)
["apple", "applesauce", "bread", "orange", "tamarind", "watermelon"]

DOCSTRING:
__________

Yes. Docstrings are needed.

DOCTESTS:
_________

Yes. Two doctests are needed.

UNIT TESTS:
___________

No. No unit tests are needed.

MAIN FUNCTION AND IF-STATEMENT BELOW IT
_______________________________________

Yes. The main function should invoke your function with a simple example.

"""


def merge(first, second):
    """
    Merge and sort two lists.

    :param first: a list which is pre-sorted and the same type with second
    :param second:  a list which is pre-sorted and the same type with first
    :precondition: two lists (first and second) are pre-sorted
    :precondition: two lists (first and second) are homogenous
    :precondition: elements in two lists (first and second) are sortable
    :postcondition: merges and sorts two lists
    :return: a new sorted list that contains the elements from first and second

    >>> first_list = [1, 2, 3]
    >>> second_list = [-1, 4, 5]
    >>> merge(first_list, second_list)
    [-1, 1, 2, 3, 4, 5]

    >>> first_list_2 = [1, 2, 100]
    >>> second_list_2 = [-5, 90]
    >>> merge(first_list_2, second_list_2)
    [-5, 1, 2, 90, 100]
    """
    result = []
    while len(first) > 0 or len(second) > 0:
        if len(first) > 0 and len(second) > 0:
            if first[0] <= second[0]:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        elif len(first) > 0:
            result += first
            first = []
        elif len(second) > 0:
            result += second
            second = []
    return result


def main():
    some_list = [1, 5, 9]
    some_other_list = [-10, 44, 100]
    sorted_merge = merge(some_list, some_other_list)
    print(sorted_merge)

    some_list_2 = ["apple", "orange", "tamarind"]
    some_other_list_2 = ["applesauce", "bread", "watermelon"]
    sorted_merge_2 = merge(some_list_2, some_other_list_2)
    print(sorted_merge_2)


if __name__ == "__main__":
    main()
