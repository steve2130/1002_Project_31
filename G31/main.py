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
            user_IO.EmojiPrint("\033[0;31m:(\033[0;0m", "Please check your entered option. It should be a number between 1 and 3.")





def Menu_selection(option):
    if (main_checkDataFileExistence() == True):

            if option == 1:
                Record()

            elif option == 2:
                Update()

            elif option == 3:
                View()

            else:
                user_IO.EmojiPrint("\033[0;31m:(\033[0;0m", "Please check your entered option. It should be a number between 1 and 3.")
    
    elif (main_checkDataFileExistence() == False):
        main()





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
        user_IO.EmojiPrint("\033[0;31m:(\033[0;0m", "Cannot find the data file.")
        user_IO.IndentPrint("Would you like to create a new data file? (Y / N)")

        checkflag = False

        while (checkflag == False):    # To loop this part if the user entered char != Y / N
            option = input(">> ")

            if option.upper() == "Y" or option.upper() == "YES":
                checkflag = True                                        
                csv_IO.CSV_creation()
                user_IO.EmojiPrint("\033[0;32m:)\033[0;0m", "\033[2;32mData file created!\033[0;0m\n")

                return False   # So that it will return to the main menu after the file is created.


            elif option.upper() ==  "N" or option.upper() == "NO":
                checkflag = True
                print(" ")  # line break
                return False   # return to main menu

            else:
                user_IO.EmojiPrint("\033[0;31m:(\033[0;0m", " Please check the word you have entered. It should be a character of either Y or N.")





def Record():
    entry = user_IO.Record_userInput()
    csv_IO.CSV_writeToFile(entry)
    user_IO.EmojiPrint("\033[0;32m:)\033[0;0m", "\033[0;32mRecorded!\033[0;0m")
    user_IO.View_getCurrentBalance(False)





def Update():
    
    print(" ")      # line break
    column_header = user_IO.Update_getColumnHeader()
    row_data = csv_IO.CSV_retrieveEntireListOfEntries()     # entire list with header and in original order
    entries = user_IO.Update_getEntries()                   # list without header and in reverse order

    if (entries == False):
        user_IO.EmojiPrint("\033[0;31m:(\033[0;0m", "No data in data.csv. Cannot update.")

    else:
        user_IO.Update_printEntries(column_header, entries)

        entry_number = user_IO.Update_getEntryNumber(len(entries))      # Just to stop user to enter a number bigger than the length of entries
        entry_column = user_IO.Update_getIntentedHeader()
        edit_content = user_IO.Update_processEntryColumn(entry_column)      # [0] = content to be edited     [1] = index of the column in .csv


        if (edit_content == False):     # for deleteing entry
            del row_data[(len(row_data) - entry_number)]

        elif (type(edit_content) == list):
            row_data[(len(row_data) - entry_number)][edit_content[1]] = str(edit_content[0])
                        #  ^^^ Because the displayed list is reverse, we need to retrive the correct entry using this

            # e.g. user select the the first entry from the list. Pick the corresponding column (cathgory) using {edit_content[1]}. Change its content to {edit_content[0]}




        row_data = [','.join(x) for x in row_data]      # As row_data is a lists in list, this converts the lists inside the overall list to string
                                                        # [['User Entered Date', 'Income', 'Category', 'Name', 'Amount'], ['2022-11-15', 'False', 'Kfc', 'kfc', '15000.0'], ['2022-11-15', 'False', 'Food', 'KFC', '4.0']]
                                                        #  ↓
                                                        # ['User Entered Date,Income,Category,Name,Amount', '2022-11-15,False,Kfc,kfc,15000.0', '2022-11-15,False,Food,KFC,4.0']
                                                        # https://stackoverflow.com/questions/22105741/converting-a-list-of-lists-into-a-list-of-strings-python
        
        row_string = "\n".join(row_data)                #  ↓
                                                        # 'User Entered Date,Income,Category,Name,Amount\n2022-11-15,False,Kfc,kfc,15000.0\n2022-11-15,False,Food,KFC,4.0\n2022-11-15,True,Salary,HAS,15000.0'

        csv_IO.CSV_overwriteToFile(row_string)
        # https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python

        user_IO.EmojiPrint("\n\t\033[0;32m:)", "Updated!\033[0;0m")
        user_IO.View_getCurrentBalance(False)





def View():
    user_IO.FunctionIndentPrint("")     # line break

    view_options = {
        1: "Balance",
        2: "Yearly income",
        3: "Top 3 spending in past 30 days"
    }

    user_IO.FunctionIndentPrint("\033[3;33;42mView your income / expense here!\033[0;0;0m\n")
    for key in view_options.keys():
        print("\t\t(", key, ") － ", view_options[key], sep = "")


    # User input
    try:        
        option = int(input("\t>> "))


        if  (option == 1):  # Balance
            user_IO.View_getCurrentBalance(True)

        elif(option == 2):  # Yearly income
            print("")

        elif(option == 3):  # Top 3 spending in past 30 days
            user_IO.Top_ThreeSpendings()

        else:
            user_IO.EmojiPrint("\033[0;31m:(\033[0;0m", "I am not quite sure that you've entered the correct option...")

    except:
        user_IO.EmojiPrint("\033[0;31m:(\033[0;0m", "I am not quite sure that you've entered the correct option...")




if __name__ == "__main__":
    main()