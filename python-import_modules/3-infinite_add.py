#!/usr/bin/python3

import sys


def main():
    argv = sys.argv[1:]
    argc = len(argv)

    print(sum(int(argv[i])))


if __name__ == "__main__":
    main()
