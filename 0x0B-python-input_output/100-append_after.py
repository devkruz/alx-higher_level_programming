#!/usr/bin/python3
"""Search and replace word in file"""


def append_after(filename="", search_string="", new_string=""):
    """Search and replace word in file"""

    new_content = []
    with open(filename, encoding="utf-8") as file:
        for fileline in file:
            new_content.append(fileline)
            if search_string in fileline:
                new_content.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write("".join(new_content))
