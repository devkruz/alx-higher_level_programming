#!/usr/bin/python3

"""
adds all arguments to
a Python list,
and then save
them to a file

"""
from sys import argv


def main():
    """
    adds all arguments to
    a Python list,
    and then save
    them to a file

    """

    if __name__ == "__main__":
        save_to_json = __import__('5-save_to_json_file')\
            .save_to_json_file
        load_from_json = __import__("6-load_from_json_file")\
            .load_from_json_file

        try:
            a_list = load_from_json("add_item.json")
        except FileNotFoundError:
            a_list = []
        else:
            if not isinstance(a_list, list):
                raise TypeError("Expecting a list")
        finally:
            a_list.extend(argv[1:])
            save_to_json(a_list, "add_item.json")


main()
