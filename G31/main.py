import csv_IO as csv_IO
import user_IO as user_IO





def main():
    """
        Hello! This expense tracker helps you to keep track of your incomes and expenses.
        How can I help you?
    """
    print(main.__doc__)
    while(1):               # Just to loop infinitely
        Menu_printOptions()

        # Error exception.
        # To check whether the user entered a number or a string
        # throw an error text if user entered a string

        try:        
            option = int(input(">> "))
            Menu_selection(option)

        except:
            user_IO.EmojiPrint(":(", "Please check your entered option. It should be a number between 1 and 3.")





def Menu_selection(option):
    if (main_checkDataFileExistence() == True):

            if option == 1:
                Record()

            elif option == 2:
                Update()

            elif option == 3:

                View()

            else:
                user_IO.EmojiPrint(":(", "Please check your entered option. It should be a number between 1 and 3.")
    
    elif (main_checkDataFileExistence() == False):
        return





def Menu_printOptions():
    """Just to provide a space to quickly edit options' order and text in the menu"""
    # https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/


    user_IO.IndentPrint("Main menu")
    user_IO.IndentPrint("－－－－－－－－－－－－－－－－－－－－－")
    menu_options = {
        1: "Record",
        2: "Update",
        3: "View"
    }

    for key in menu_options.keys():
        print("\t[", key, "] － ", menu_options[key], sep = "")  # sep is needed so I can use \t 

    user_IO.IndentPrint("－－－－－－－－－－－－－－－－－－－－－")





def main_checkDataFileExistence():
    """
    Check the existence of data.csv

    return True if data.csv exists
    if data.csv does not exist
        -> Ask user whether they want to create a new data.csv or not
        -> return to main menu regardless data.csv is created or not
    """

    if (csv_IO.CSV_checkFileExistence() == True):
        return True

    else:
        user_IO.EmojiPrint(":(", "Cannot find the data file.")
        user_IO.IndentPrint("Would you like to create a new data file? (Y / N)")

        checkflag = False

        while (checkflag == False):    # To loop this part if the user entered char != Y / N
            option = input(">> ")

            if option.upper() == "Y" or option.upper() == "YES":
                checkflag = True                                        
                csv_IO.CSV_creation()
                user_IO.LineBreakPrint("Data file created!\n")

                return False   # So that it will return to the main menu after the file is created.


            elif option.upper() ==  "N" or option.upper() == "NO":
                checkflag = True
                print(" ")  # line break
                return False   # return to main menu

            else:
                user_IO.EmojiPrint(":(", " Please check the word you have entered. It should be a character of either Y or N.")





def Record():
    entry = Record_userInput()
    csv_IO.CSV_writeToFile(entry)
    user_IO.EmojiPrint(":)", "Recorded!")






def Record_userInput():
    """
    Record user's inputs and store them in data.csv

    Input: refer to {CSV_getDefaultRowItems()} in csv_IO.py 
    Output: nothing
    """
    print(" ")
    user_IO.FunctionIndentPrint("🡫 🡫 🡫")
    user_IO.FunctionIndentLineBreakPrint("Record your income or spending here!")

    timestamp = csv_IO.Time_UTCDateAndTime()
    income = user_IO.Record_userInput_Income()
    category = user_IO.Record_userInput_Category()
    name = user_IO.Record_userInput_Name(category)
    amount = user_IO.Record_userInput_Amount()
    date = user_IO.Record_userInput_Date()

    entry = {
        "Entry created time": timestamp,
        "Income" : income,
        "Category" : category,
        "Name" : name,
        "Amount" : amount,
        "User entered time" : date
    }

    return entry



    


def Update():
    row_header = csv_IO.CSV_getDefaultRowItems()
    row_header[0] = "Date"                  # Remove timestamp (uuid) and replaced with {User entered time}
    del row_header[5]


    row_data = csv_IO.CSV_retrieveEntireListOfEntries()
    if (row_data != []):
        row_data.reverse()                      # To get the latest entries first

        for i in range(0, len(row_data)):
            row_data[i][0] = row_data[i][5]     # replace timestamp with {User entered time}
            del row_data[i][5]                  # delete {User entered time}
            # print(row_data[i])



        # https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

        row_header_format = "{:>20}" * (len(row_header))               # {:>20} -> each header takes 20 spaces 
        row_data_format = "{:>20}" * (len(row_data[0]))

        print("\t    ", row_header_format.format(*row_header), sep="")        # * = all elements in the list
                                                                              # \t somehow == 8 spaces here
        print("\t", "－" * 52, sep="")                                # 5*(20/2)+2 = 52. +2 because the spaces above "\t    ". 
                                                                                                                 #      ^^^^ 
                                                                      # "－" is full-width character, uses two half-width spaces
        for i in range(0, (len(row_data))):
            print(f"\t({i + 1}) ", row_data_format.format(*row_data[i]), sep="")        # Will be a mess if user entered a long string for category or name

        print("\t", "－" * 52, "\n", sep="")




    else:
        user_IO.EmojiPrint(":(",  "No data in data.csv. Cannot update.")







def View():
        row_data = csv_IO.CSV_retrieveEntireListOfEntries()
        print(row_data)
        # Your current balance
        











if __name__ == "__main__":
    main()