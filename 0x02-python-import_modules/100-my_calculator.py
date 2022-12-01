#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    arg_len = len(argv)

    if arg_len < 3:
        print("{} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operator = [["+", add],["-", sub], ["*", mul], ["/", div], ["null"]]

    for op in operator:
        if op[0] == argv[2]:
            print("{} {} {} = {}"
            .format(argv[1], argv[2], argv[3], op[1](argv[1], argv[3])))
            break;
        elif op[0] == "null":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
