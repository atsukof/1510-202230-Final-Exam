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
    Create a backup file with .bak extension.

    :param file_name: a string of a file name
    :precondition: a file with file_name must exist.
    :return:
    """
    try:
        with open(file_name) as file_object:
            all_text = file_object.read()
    except FileNotFoundError:
        print("File does not exist.")
    else:
        if file_name[-4:] == ".txt":
            new_file_name = file_name[:-4] + ".bak"
        else:
            new_file_name = file_name

        with open(new_file_name, 'w') as another_object:
            another_object.write(all_text)

        print(f"generated {new_file_name}.")


def main():
    backup("test.txt")
    backup("test2.txt")


if __name__ == "__main__":
    main()
