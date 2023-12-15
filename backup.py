"""
(4 points) Implement a function called backup.

           The backup function accepts a string, the name of a file. This function must create
           a duplicate file with the same content but if the name of the file includes an
           extension, you must replace the extension with .bak.

           When it is done, the backup function must print a helpful confirmation message for the
           user, like this:

           backup("important_file.txt")
           generated important_file.bak

           backup("this_file_has_no_extension")
           generated this_file_has_no_extension.bak

           Make sure your function works for empty, small, and very, very large files. Make sure
           your file doesn't leave out the final newline character, or add one if there wasn't one
           in the original file. The .bak file must be identical!

(1 point) This function requires a docstring. There is no return value, but the post condition
          should state that the file has been copied in memory. No annotations are necessary.

(1 point) If the file doesn't exist, raise and document an appropriate error. Prove this works
          in the main function.
"""


def backup(file_name):
    """

    :param file_name:
    :return:
    """

def main():
    pass


if __name__ == "__main__":
    main()
