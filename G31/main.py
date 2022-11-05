# main.py

import Expense_tracker_data_IO as data_IO
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
        checkflag_category = False
        checkflag_amount = False
        checkflag_date = False

        # My brain hurts...
        #####################################
        while(checkflag_income == False):       # loop if the user mis-input something like int or bool here
            
            FunctionIndentLineBreakPrint("\033[3;33;40mIncome (I) or Expense (E)?\033[0;0m")
            # colored text baby
            # https://stackabuse.com/how-to-print-colored-text-in-python/

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


        #####################################
        while(checkflag_category == False):
            FunctionIndentLineBreakPrint("\033[3;33;40mWhich category does it belong? (e.g. Breakfast, Shopping, Salary)\033[0;0m")

            category = input("\t>> ")

            if (re.match("[a-zA-Z]", category)):                      # regex. Return true if it find a character in {category}. 
                                                                    # Return false if number is place before characters. like "6x crab", "7x beer"
                category = category[0].upper() + category[1:]       # Capitalize the first letter of {category}
                checkflag_category = True
            
            else:
                FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter a word as a category.")
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
            #     FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter a word as a category.")
            #     checkflag_category = False

            # # This code will throw exception if a string exist in {category} and cannot be converted into float/int/bool/complex
            # # Which is a good thing because we do need a string and not numbers
            # # If the user actually typed a number (int/float), it will then processed with the code in "else:", as the number user entered cannot trigger an type error

            # # Only string will trigger an error, which is what we want
            # # Will 100% get blame if used in production code.




        #####################################
        while(checkflag_amount == False):
            FunctionIndentLineBreakPrint("\033[3;33;40mHow much is that?\033[0;0m")

            try: 
                amount = float(input("\t>> $"))
                amount = round(amount, 2)       # round the $ to 2 dec place -> 200.689 -> 200.69
                checkflag_amount = True
            
            except:
                FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter a number.")
                checkflag_amount = False


        #####################################
        # ***Not Working!!!***
        while(checkflag_date == False):
            FunctionIndentLineBreakPrint("\033[3;33;40mWhen did it happen?\033[0;0m")
            FunctionIndentPrint(" - \033[3;33;40mIf it happens today, type 'T' or 'Today'.\033[0;0m")
            FunctionIndentPrint(" - \033[3;33;40mIf it happened in the past, type the date (YYYY-MM-DD) it happens.\033[0;0m")

            date = str(input("\t>> "))

            if (date.upper() == "T" or date.upper() == "TODAY"):
                date = data_IO.Time_LocalDate()     # Get today date
                checkflag_date = True


            # ***Not Working!!!***
            elif (re.search("[-]", date)):     # To find "-" in 2022-11-05     -> Just to avoid someone mis-input the date like 2022/11/05
            # ***Not Working!!!***    
                try:
                    check_date = date.split("-")

                    check_date[0] = int(check_date[0])
                    check_date[1] = int(check_date[1])
                    check_date[2] = int(check_date[2])

                    # ***Not Working!!!***
                    if (len(check_date[0]) == 4 and len(check_date[1]) == 2 and len(check_date[2]) == 2 and check_date[1] <= 12 and check_date[2] <= 31):
                        # check for length of YYYY, MM, DD and whether MM > 12 or DD > 31
                        checkflag_date = True
                    # ***Not Working!!!***       
                    else:
                        FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter either 'T' / 'Today', or a vaild date (YYYY-MM-DD).")
                        checkflag_date = False

                except:
                    FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter either 'T' / 'Today', or a vaild date (YYYY-MM-DD).")
                    checkflag_date = False
                



            else:
                FunctionIndentPrint("\033[1;31;40m[🗙 ]\033[0;0m Invaild input. Please enter either 'T'/'Today', or a vaild date (YYYY-MM-DD).")
                checkflag_date = False


        #####################################
        entry = {
            "Entry created time": data_IO.Time_UTCDateAndTime(),
            "Income" : income_boolean,
            "Category" : category,
            "Amount" : amount,
            "User entered time" : date
        }

        print(entry)


    else:
        return # return to main menu

    


def Update():
    return




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