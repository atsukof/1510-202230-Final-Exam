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
