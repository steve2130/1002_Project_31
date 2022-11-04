# Input/store/update/retrieve the income(s), spendings and other allocations
# Tommy


import csv      
from os import path                   

def main():
    """
        This expense tracker 
    """
    csv_creation()



def csv_creation():
    """

    """
    default_row_items = ["Entry created time", "Income", "Category", "Amount", "User entered time"]
                        # Timestamp             boolean   string       float    timestamp/string?

                        
    while (path.isfile("data.csv")):
        # if data.csv does not exist

        with open("data.csv", "w") as data_csv:
            data_writer = csv.writer(data_csv)
            data_writer.writerow(default_row_items)     # write the columns of the csv with elements of {default_row_items}



    # it should skip the while loop is data.csv exists
    with open("data.csv") as data_csv:
        data_reader = csv.DictReader(data_csv)
        for i in range(1):
            line.
    
    return data_reader


def csv_readLine():
    




if __name__ == "__main__":
    main()