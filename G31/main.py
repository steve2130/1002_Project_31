# main.py

import Expense_tracker_data_IO as data_IO

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
        if option == 1:
            Record()

        elif option == 2:
            Update()

        elif option == 3:
            View()

        else:
            EmojiPrint(":(", "Please check your entered option. It should be a number between 1 and 3.")



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

                return False


            elif option.upper() ==  "N" or option.upper() == "NO":
                checkflag = True
                print(" ")  # line break
                return False

            else:
                EmojiPrint(":(", " Please check you have entered. It should be a character of either Y or N.")





def Record():
    """
    Record user's inputs and store them in data.csv

    Input: refer to {CSV_getDefaultRowItems()} in Expense_tracker_data_IO.py 
    Output: nothing
    """
    if(main_checkDataFileExistence() == True):
        print(" ")
        FunctionIndentPrint("🡫 🡫 🡫")
        FunctionIndentLineBreakPrint("Record your income or spending here!")

        # vars
        checkflag_income = False


        #################
        while(checkflag_income == False):
            
            FunctionIndentLineBreakPrint("Income (I) or Expense (E)?")
            income = input("\t>> ")

            if income.upper() == "I" or income.upper() == "INCOME":
                checkflag_income = True
                income_boolean = True

            elif income.upper() == "E" or income.upper() == "EXPENSE":
                checkflag_income = True
                income_boolean = False

            else:
                FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter either 'I' or 'E'.\n")
                checkflag_income == False


        #################
        FunctionIndentLineBreakPrint("Which category does it belong? (e.g. Breakfast, Shopping, Salary)")
        try: 
            category = str(input("\t>> "))

        except:
            FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter a word as a category.")    # pretty pointless

        
        
        #################
        FunctionIndentLineBreakPrint("How much is that?")
        try:
            amount = float(input("\t>> "))
            amount = round(amount, 2)
            print(amount)

        except:
            FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter a number.")


        #################
        entry = {
            "Entry created time": data_IO.Time_UTCDateAndTime(),
            "Income" : income_boolean,
            "Category" : category
        }

    else:
        return # return to main menu

    







def View():
    if(main_checkDataFileExistence() == True):
        row_data = data_IO.CSV_retreveEntireListOfEntries()

        # Your current balance
        
    else:
        return  # return to main menu








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