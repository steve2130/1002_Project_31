# If you are using VS Code and you are debugging with breakpoints,
# you might want to disable JustMyCode in launch.json
# Otherwise csv.DictReader and csv.DictWriter so how what do not work.

# https://stackoverflow.com/questions/52980448/how-to-disable-just-my-code-setting-in-vscode-debugger



import data_IO as data_IO
import re

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
            EmojiPrint(":(", "Please check your entered option. It should be a number between 1 and 3.")




def Menu_selection(option):
    if (main_checkDataFileExistence() == True):

            if option == 1:
                Record()

            elif option == 2:
                Update()

            elif option == 3:

                View()

            else:
                EmojiPrint(":(", "Please check your entered option. It should be a number between 1 and 3.")
    
    elif (main_checkDataFileExistence() == False):
        return


def Menu_printOptions():
    """Just to provide a space to quickly edit options' order and text in the menu"""
    # https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/


    IndentPrint("Main menu")
    IndentPrint("－－－－－－－－－－－－－－－－－－－－－")
    menu_options = {
        1: "Record",
        2: "Update",
        3: "View"
    }

    for key in menu_options.keys():
        print("\t[", key, "] － ", menu_options[key], sep = "")  # sep is needed so I can use \t 

    IndentPrint("－－－－－－－－－－－－－－－－－－－－－")





def main_checkDataFileExistence():
    """
    Check the existence of data.csv

    return True if data.csv exists
    if data.csv does not exist
        -> Ask user whether they want to create a new data.csv or not
        -> return to main menu regardless data.csv is created or not
    """

    if (data_IO.CSV_checkFileExistence() == True):
        return True

    else:
        EmojiPrint(":(", "Cannot find the data file.")
        IndentPrint("Would you like to create a new data file? (Y / N)")

        checkflag = False

        while (checkflag == False):    # To loop this part if the user entered char != Y / N
            option = input(">> ")

            if option.upper() == "Y" or option.upper() == "YES":
                checkflag = True                                        
                data_IO.CSV_creation()
                LineBreakPrint("Data file created!\n")

                return False   # So that it will return to the main menu after the file is created.


            elif option.upper() ==  "N" or option.upper() == "NO":
                checkflag = True
                print(" ")  # line break
                return False   # return to main menu

            else:
                EmojiPrint(":(", " Please check the word you have entered. It should be a character of either Y or N.")





def Record():
    entry = Record_userInput()
    data_IO.CSV_writeToFile(entry)
    EmojiPrint(":)", "Recorded!")






def Record_userInput():
    """
    Record user's inputs and store them in data.csv

    Input: refer to {CSV_getDefaultRowItems()} in Expense_tracker_data_IO.py 
    Output: nothing
    """

    print(" ")
    FunctionIndentPrint("🡫 🡫 🡫")
    FunctionIndentLineBreakPrint("Record your income or spending here!")

    # vars
    checkflag_income = False
    checkflag_category = False
    checkflag_name = False
    checkflag_amount = False
    checkflag_date = False


    # My brain hurts...
    #####################################
    while(checkflag_income == False):       # loop if the user mis-input something like int or bool here
        
        FunctionIndentLineBreakPrint("\033[3;33mIncome (I) or Expense (E)?\033[0;0m")
        # colored text baby
        # https://stackabuse.com/how-to-print-colored-text-in-python/
        # even worse than <span>...

        income = input("\t>> ")

        if income.upper() == "I" or income.upper() == "INCOME":
            checkflag_income = True
            income_boolean = True

        elif income.upper() == "E" or income.upper() == "EXPENSE":
            checkflag_income = True
            income_boolean = False

        elif income.upper() == "EXIT":
            return

        else:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either 'I' or 'E'.\n")
            checkflag_income == False


    #####################################
    while(checkflag_category == False):
        FunctionIndentLineBreakPrint("\033[3;33mWhich category does it belong? (e.g. \033[4;36mFood\033[0;0m\033[3;33m, \033[4;36mTraffic\033[0;0m\033[3;33m, \033[4;36mShopping\033[0;0m\033[3;33m)\033[0;0m")

        category = input("\t>> ")

        if (re.match("[a-zA-Z]", category)):                    # regex. Return true if it find a character in {category}. 
                                                                # Return false if number is place before characters. like "6x crab", "7x beer"
            category = category[0].upper() + category[1:]       # Capitalize the first letter of {category}
            checkflag_category = True
        
        else:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a word as a category.")
            checkflag_category = False




        # try:
        #     category = input("\t>> ")
        #     category = complex(bool(int(float(category))))      # To give error if user entered int or float, hopefully user will not enter complex number
        #                                                                                                       # looks like it treats it as string so everything is cool
        # except:
        # # if (type(category) != str):
        #     category = category[0].upper() + category[1:]       # Capitalize the first letter of {category}
        #     checkflag_category = True

        # else:
        #     FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a word as a category.")
        #     checkflag_category = False

        # # This code will throw exception if a string exist in {category} and cannot be converted into float/int/bool/complex
        # # Which is a good thing because we do need a string and not numbers
        # # If the user actually typed a number (int/float), it will then processed with the code in "else:", as the number user entered cannot trigger an type error

        # # Only string will trigger an error, which is what we want
        # # Will 100% get blame if used in production code.





    #####################################
    while(checkflag_name == False):
        FunctionIndentLineBreakPrint("\033[3;33mWould you like to give it a name?\033[0;0m")
        FunctionIndentPrint(" - \033[3;33mFor example: (\033[4;36mFood\033[0;0m\033[3;33m - \033[4;32mKFC\033[0;0m\033[3;33m), (\033[4;36mTraffic\033[0;0m\033[3;33m - \033[4;32mbus[215X]\033[0;0m\033[3;33m), (\033[4;36mShopping\033[0;0m\033[3;33m - \033[4;32mSteam\033[0;0m\033[3;33m).\033[0;0m")
        # CSS, the most hated thing in this entire earth, is still better than this crap
        # even brainf*ck is better than this

        try: 
            name = str(input("\t>> "))
            if (name == ""):                  # Check for empty string
                name = category
                checkflag_name = True
                
            elif (name.strip() != ""):        # Check for spaces only input: "    "
                checkflag_name = True

            else:
                FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a number.")
                checkflag_name = False
        
        except:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a number.")
            checkflag_name = False





    #####################################
    while(checkflag_amount == False):
        FunctionIndentLineBreakPrint("\033[3;33mHow much is that?\033[0;0m")

        try: 
            amount = float(input("\t>> $"))
            amount = round(amount, 2)       # round the $ to 2 dec place -> 200.689 -> 200.69
            checkflag_amount = True
        
        except:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a number.")
            checkflag_amount = False





    #####################################
    # ***Not Working!!!***
    while(checkflag_date == False):
        FunctionIndentLineBreakPrint("\033[3;33mWhen did it happen?\033[0;0m")
        FunctionIndentPrint(" - \033[3;33mIf it happens today, type 'T' or 'Today'.\033[0;0m")
        FunctionIndentPrint(" - \033[3;33mIf it happened in the past, type the date (YYYY-MM-DD) it happens.\033[0;0m")

        date = str(input("\t>> "))

        if (date.upper() == "T" or date.upper() == "TODAY"):
            date = data_IO.Time_LocalDate()     # Get today date
            checkflag_date = True


        # ***Not Working!!!***
        elif (type(int(date[0])) == int):     
        # ***Not Working!!!***    
            try:
                check_date = date.split("-")    # To find ans split "-" in 2022-11-05     -> Just to avoid someone mis-input the date like 2022/11/05

                # ***Not Working!!!***
                if (len(check_date[0]) == 4 and len(check_date[1]) == 2 and len(check_date[2]) == 2 and int(check_date[1]) < 13 and int(check_date[2]) < 32 and int(check_date[0]) > 1969 and int(check_date[1]) > 0 and int(check_date[2]) > 0):
                    # check for length of YYYY, MM, DD and whether MM > 12 or DD > 31
                    checkflag_date = True
                # ***Not Working!!!***       
                else:
                    FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either 'T' / 'Today', or a vaild date (YYYY-MM-DD).")
                    checkflag_date = False

            except:
                FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either 'T' / 'Today', or a vaild date (YYYY-MM-DD).")
                checkflag_date = False
            



        else:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either 'T'/'Today', or a vaild date (YYYY-MM-DD).")
            checkflag_date = False


    #####################################
    entry = {
        "Entry created time": data_IO.Time_UTCDateAndTime(),
        "Income" : income_boolean,
        "Category" : category,
        "Name" : name,
        "Amount" : amount,
        "User entered time" : date
    }

    return entry



    


def Update():
    row_header = data_IO.CSV_getDefaultRowItems()
    row_header[0] = "Date"                  # Remove timestamp (uuid) and replaced with {User entered time}
    del row_header[5]



    row_data = data_IO.CSV_retreveEntireListOfEntries()
    row_data.reverse()                      # To get the latest entries first
    for i in range(len(row_data)):
        row_data[i][0] = row_data[i][4]     # replace timestamp with {User entered time}
        del row_data[i][4]                  # delete {User entered time}
    


    # https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

    row_header_format = "{:>12}" * (len(row_header) + 1)
    row_data_format = "{:>12}" * (len(row_data) + 1)

    print(row_header_format.format("", *row_header))
    for i in range(1, len(row_data) - 1):
        print(row_format.format("", *row_data[i]))


def View():
        row_data = data_IO.CSV_retreveEntireListOfEntries()
        print(row_data)
        # Your current balance
        







#-----------------------------------------------------------------
# Misc

# Basically just some different versions of print()
# Just want to be more organize with the printed string
def IndentPrint(string):
    print("\t", str(string), sep="")

def LineBreakPrint(string):
    print("\n\t", str(string), "\n", sep="")

def EmojiPrint(emoji, string):
    print("\n     ", str(emoji), " ", str(string), "\n", sep="")

def FunctionIndentPrint(string):
    # For sub-functions e.g. Record(), Update(), View()
    print("\t\t", str(string), sep="")

def FunctionIndentLineBreakPrint(string):
    print("\n\t\t", str(string), sep="")



if __name__ == "__main__":
    main()