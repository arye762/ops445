#!/usr/bin/env python3
# Student ID: ACimafranca

import sys

def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.readlines()
        file.close()
        return contents
    except FileNotFoundError:
        return ["File not found!"]

def main():
    if len(sys.argv) < 2:
        print("Error: no file specified.")
        return

    filename = sys.argv[1]
    contents = read_file(filename)

    if contents == ["File not found!"]:
        print(contents[0])
        print("Number of lines: 1")
    else:
        for line in contents:
            print(line, end='')  # end='' to avoid adding extra newline characters
        print("Number of lines:", len(contents))

if __name__ == '__main__':
    main()
