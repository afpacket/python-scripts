#!/usr/bin/env python3

import pandas
from argparse import ArgumentParser
from tabulate import tabulate

def main():
   parser = ArgumentParser()
   parser.add_argument("filename", type=str,
                       help="csv filename to parse")
   args = parser.parse_args()

   filename = args.filename

   try:
       with open(filename) as csv_file:
            csv_to_table(csv_file)

   except EnvironmentError as error:
          print(f"error: {error}")

def csv_to_table(csv_file):
    """Read csv file and output as a table"""

    try:
        data = pandas.read_csv(csv_file, index_col=0)
        print(tabulate(data, headers=data.columns, tablefmt="grid"))

    except Exception as error:
           print(f"error: {error}")
           
if __name__ == "__main__":
   main()
