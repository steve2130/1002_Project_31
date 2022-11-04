# Input/store/update/retrieve the income(s), spendings and other allocations
# Tommy


import csv      
from os import path                   

def main():
    """
        This expense tracker 
    """
    csv_read()



def csv_creation():
    default_row_items = ["Entry created time", "Income", "Category", "Amount", "User entered time"]
                        # Timestamp             boolean   string       float    timestamp/string?
        
    if (path.isfile("data.csv") != True):   # check if data.csv does not exist
        
        with open("data.csv", "w") as data_csv:
            data_writer = csv.writer(data_csv)
            data_writer.writerow(default_row_items)     # write the columns of the csv with elements of {default_row_items}





def csv_read():

    default_row_items = ["Entry created time", "Income", "Category", "Amount", "User entered time"]
                        # Timestamp             boolean   string       float    timestamp/string?
    with open("data.csv") as data_csv:

        if (csv_readSingleLine(data_csv, default_row_items)):
            data_reader = csv.DictReader(data_csv)

        else:
            csv_creation()
    
    return data_reader





def csv_readSingleLine(data_csv, default_row_items):
    for i in range(1, 2):
        line = data_csv.readline()

        if line == default_row_items:
            return True

        else:
            return False



if __name__ == "__main__":
    main()