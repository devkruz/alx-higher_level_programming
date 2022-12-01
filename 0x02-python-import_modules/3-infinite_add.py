#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    arg_len = len(argv) - 1
    result = 0
    if arg_len > 1:
        for arg in range(1, (arg_len + 1)):
            result += int(argv[arg])
    print("{}".format(result))
5
