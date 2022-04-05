# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from distutils.log import error
from genericpath import exists
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.


    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualifying_loans, csvpath) :
    """Writes the qualifying loans into CSV in the path provided


    Args:
        csvpath (Path): The csv file path.
        qualifying_loans : Lists qualifying loans to write into csv 

    """  

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

            # Loop through the qualifying loans list 
            # Write to the file
        for loan in qualifying_loans:
            csvwriter.writerow(loan) 















        


