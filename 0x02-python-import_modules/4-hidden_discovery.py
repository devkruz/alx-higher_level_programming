#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    atribute = dir(hidden_4)

    for name in atribute:
        if name[:2] != "__":
            print(name)
