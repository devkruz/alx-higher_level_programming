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
        save_to_json = __import__('5-save_to_json_file.py')\
            .save_to_json_file
        load_from_json = __import__("6-load_from_json_file.py")\
            .load_from_json_file

        try:
            list = load_from_json("add_item.json")
        except FileNotFoundError:
            list = []
        finally:
            list.extend(argv[1:])
            save_to_json(list, "add_item.json")

main()