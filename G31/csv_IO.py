# Input/store/update/retrieve the income(s), spendings and other allocations
# Tommy


import csv      
from os import path
from datetime import datetime                   # need the date
import time                                     # Unix time epoch


def CSV_getDefaultRowItems():
    """Just to avoid creating var {Default_row_items} every time I want to use it"""
    return ["Entry created time", "Income", "Category", "Name", "Amount", "User entered time"]
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

            # Name:               String 
            #                     For user to name their income / spending

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
    # https://stackoverflow.com/questions/58992872/how-to-create-a-csv-file-in-python-script-if-it-doesnt-exist-in-the-directory
    default_row_items = CSV_getDefaultRowItems()
    
    with open("data.csv", "w") as data_csv:
        data_writer = csv.writer(data_csv)
        data_writer.writerow(default_row_items)     # write the columns of the csv with elements of {default_row_items}





def CSV_retrieveEntireListOfEntries():
    """
        Retrieve all entries in data.csv 

        Input: nothing
        Output: [[a row of data in data.csv], [another row of data in data.csv], ...] 
    """
    row_data = []

    # How to write or read csv
    # https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/
    with open("data.csv", "r") as data_csv:
        data_reader = csv.DictReader(data_csv, fieldnames=CSV_getDefaultRowItems())

        for row in data_reader:
                row_data.append([row["Entry created time"], row["Income"], row["Category"], row["Name"], row["Amount"], row["User entered time"]])
        
        return row_data




def CSV_writeToFile(entry):
    with open("data.csv", "a") as data_csv:
        # "r" or "w" or "a"
        # https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
        data_writer = csv.DictWriter(data_csv, fieldnames=CSV_getDefaultRowItems())
        data_writer.writerow(entry)

        # **Will bugged if another process (e.g. excel) is opening data.csv

        # print("\n\t :( Something is wrong with writing to the data file.\n")





def CSV_overwriteToFile(data):
    """
        For updating the entries
        .csv cannot edit one element at a time
        it must overwrites the entire .csv 
    """
    # https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python
    with open("data.csv", "w") as data_csv:
        # overwriting the entire thing so "w"
        data_writer = csv.writer(data_csv)
        data_writer.writerows(data)





# Time
def Time_UTCDateAndTime():
    """Return current UTC time in seconds"""
    return int(time.time())

def Time_LocalDate():
    """Return current local date"""
    # https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
    return str(datetime.today().strftime('%Y-%m-%d'))