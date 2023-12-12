"""

FUNCTION:
_________

Define a function called zen. This function does not accept any parameters and does not return
anything.

The zen function must open and make a copy of the file called zen.txt, which is included in the exam
package. The copy must be named zen_copy.txt. Your copy must contain the following two changes:

A) The 19 aphorisms (sayings) which end with a period must be sorted alphabetically in the
zen_copy.txt file
B) The 19 aphorisms must also be numbered like this (note the period and space after the
numbers):

1. Although never is often better than *right* now.
2. Although practicality beats purity.
3. Although that way may not be obvious at first unless you're Dutch.

...and so on...

Note that for full marks your code must follow best practices, i.e., minimize the amount of code
in a try-block.

ASSUMPTIONS (PRECONDITIONS):
____________

There is a plaintext file called zen.txt in the same folder as fun.py.

DOCSTRING:
__________

No. Docstrings are not needed.

DOCTESTS:
_________

No. No doctests are needed.

UNIT TESTS:
___________

No. No unit tests are needed.

MAIN FUNCTION AND IF-STATEMENT BELOW IT
_______________________________________

Yes. The main function should invoke your function, so I can execute your code and examine zen_copy.txt

"""


def zen():
    with open('zen.txt') as file_object:
        lines = file_object.readlines()
        print(lines)

    sayings = []
    new_lines = []
    for line in lines:
        if (line[-2:]) != ".\n":
            new_lines.append(line)
        else:
            sayings.append(line)
        sayings.sort()

    # enumerate使うやり方
    for index, value in enumerate(sayings, 1):
        new_lines.append(str(index) + ". " + value)

    # enumerate使わないやり方
    # index = 0
    # while index < len(sayings):
    #     sayings[index] = str(index + 1) + ". " + sayings[index]
    #     index += 1
    # new_lines += sayings

    print(new_lines)
    new_text = ''.join(new_lines)

    with open('zen_copy.txt', 'w') as new_file:
        new_file.write(new_text)


def main():
    zen()


if __name__ == "__main__":
    main()
