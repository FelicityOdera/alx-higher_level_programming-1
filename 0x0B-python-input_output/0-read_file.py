#!/usr/bin/python3
"""
Contains a function that reads a text file
"""

def read_file(filename=""):def read_file(filename=""):
    """reads a text file and prints it out"""
    with open(filename, "r", encoding=("utf-8")) as f:
        read_data = f.read()
    print(read_data, end='')
