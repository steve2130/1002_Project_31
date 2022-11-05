# Input/store/update/retrieve the income(s), spendings and other allocations
# Tommy


import csv      
from os import path
from datetime import datetime                   # need the date
import time                                     # Unix time epoch



def CSV_getDefaultRowItems():
    """Just to avoid creating var {Default_row_items} every time I want to use it"""
    return ["Entry created time", "Income", "Category", "Amount", "User entered time"]
            # Timestamp            boolean   string      float      timestamp/string?



            # Entry created time: String
            #                     Timestamp when the entry of this record is created.
            #                     **UTC Time**

            # Income:             Boolean
            #                     True if the record is cathgored as income
            #                     False if the record is cathgored as expense  

            # Category:           String
            #                     Entered by user to describe their income / spending
            #                     e.g. salary, food, shopping, drinks, stock interest

            # Amount              Float
            #                     Dollars

            # User entered time:  String
            #                     A date that user enter to indicate the actual date the entry occured
            #                     e.g. User enter 2022-11-05 in this column when this entry is created in 2022-11-07
            #                     To give user a option to add back the record if they forgot to add rightaway
            #                     **Local time**




def CSV_checkFileExistence():
    """Check if data.csv exist in the path of .py files"""
    return path.isfile("data.csv")
    


def CSV_creation():
    """Create .csv file if there isn't one"""
    default_row_items = CSV_getDefaultRowItems()
    
    with open("data.csv", "w") as data_csv:
        data_writer = csv.writer(data_csv)
        data_writer.writerow(default_row_items)     # write the columns of the csv with elements of {default_row_items}





def CSV_retreveEntireListOfEntries():
    """
        Retreve all entries in data.csv 

        Input: nothing
        Output: [[a row of data in data.csv], [another row of data in data.csv], ...] 
    """
    #var
    row_data = []

    with open("data.csv") as data_csv:
        data_reader = csv.DictReader(data_csv)

        for row in data_reader:
                row_data.append([row["Entry created time"], row["Income"], row["Category"], row["Amount"], row["User entered time"]])
        
        return row_data




def CSV_writeToFile(entry):
    with open("data.csv", "w") as data_csv:
        data_writer = csv.DictWriter(data_csv)











# Time
def Time_UTCDateAndTime():
    """Return current UTC time in seconds"""
    return int(time.time())