#!/usr/bin/env python3

import csv
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("filename", type=str,
                    help="csv filename to parse")
parser.add_argument("-c", "--column", type=int, dest='column_number',
                    default=0, help="the column number to parse (default=0)")
args = parser.parse_args()

csv_filename = args.filename
column_number = args.column_number 

def csv_parse(csv_file, column_number=0):
    """Read elements from specified column in CSV file and add them to list"""
    csv_reader = csv.reader(csv_file, delimiter=',')
    column_elements = []
    next(csv_reader) # skip first row so that we don't parse column name

    for row in csv_reader:
        column_elements.append(row[column_number])

    return column_elements

if __name__ == "__main__": # pronounced dunder main

   with open(csv_filename) as csv_file:
        column = csv_parse(csv_file, column_number)
        print(f'Column elements (sorted): {sorted(column)}')
        print(f'Min value element (length): {min(column, key=len)}')
        print(f'Max value element (length): {max(column, key=len)}')
