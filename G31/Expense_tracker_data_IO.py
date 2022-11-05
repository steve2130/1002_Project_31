# Input/store/update/retrieve the income(s), spendings and other allocations
# Tommy


import csv      
from os import path
from datetime import datetime                   




def csv_checkFileExistence():
    """Check if data.csv exist in the path of .py files"""
    return path.isfile("data.csv")
    


def csv_creation():
    """Create .csv file if there isn't one"""
    default_row_items = csv_getDefaultRowItems()
    
    with open("data.csv", "w") as data_csv:
        data_writer = csv.writer(data_csv)
        data_writer.writerow(default_row_items)     # write the columns of the csv with elements of {default_row_items}



def csv_getDefaultRowItems():
    """Just to avoid creating var {Default_row_items} every time I want to use it"""
    return ["Entry created time", "Income", "Category", "Amount", "User entered time"]
            # Timestamp            boolean   string      float      timestamp/string?



def csv_read():

    with open("data.csv") as data_csv:
        data_reader = csv.DictReader(data_csv)
        row_data = csv_convertRowsToLists(data_reader)
        print(row)



def csv_convertRowsToLists(data_reader):
    row_data = []
    for row in data_reader:
            row_data.append([row["Entry created time"], row["Income"], row["Category"], row["Amount"]])
    
    return row_data





