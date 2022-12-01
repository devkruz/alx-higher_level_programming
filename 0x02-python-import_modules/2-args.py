#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    arg_len = len(argv) - 1
    if arg_len > 1:
        print("{:d} arguments:".format(arg_len))
        for arg in range(1, (arg_len + 1)):
            print("{}: {}".format(arg, argv[arg]))
    elif arg_len == 1:
        print("{:d} argument:".format(arg_len))
        print("{}: {}".format(arg_len, argv[arg_len]))
    else:
        print("0 arguments.")
