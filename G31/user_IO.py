# user_IO
# Tommy
# My brain hurts...

import main
import csv_IO as csv_IO
import re




# Record()
########################################################################################################
def Record_userInput_Income():
    checkflag_income = False

    while(checkflag_income == False):       # loop if the user mis-input something like int or bool here
        
        FunctionIndentLineBreakPrint("\033[3;33mIncome (I) or Expense (E)?\033[0;0m")
        # colored text baby
        # https://stackabuse.com/how-to-print-colored-text-in-python/
        # even worse than <span>...

        income = input("\t>> ")

        if income.upper() == "I" or income.upper() == "INCOME":
            checkflag_income = True
            return True

        elif income.upper() == "E" or income.upper() == "EXPENSE":
            checkflag_income = True
            return False


        elif income.upper() == "EXIT":
            main.main()                          # back to main menu

        else:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either 'I' or 'E'.\n")
            checkflag_income == False





def Record_userInput_Category():
    checkflag_category = False

    while(checkflag_category == False):
        FunctionIndentLineBreakPrint("\033[3;33mWhich category does it belong? (e.g. \033[4;36mFood\033[0;0m\033[3;33m, \033[4;36mTraffic\033[0;0m\033[3;33m, \033[4;36mShopping\033[0;0m\033[3;33m)\033[0;0m")

        category = input("\t>> ")

        if (re.match("[a-zA-Z]", category)):                    # regex. Return true if it find a character in {category}. 
                                                                # Return false if number is place before characters. like "6x crab", "7x beer"
            category = category[0].upper() + category[1:]       # Capitalize the first letter of {category}

            if (len(category) > 26):
                FunctionIndentPrint("\033[3;35mUmm...\033[0;0m You can only enter no more than 25 characters here. Sorry!")
                checkflag_category = False
        
            else:
                checkflag_category = True
                return category

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





def Record_userInput_Name():
    checkflag_name = False

    while(checkflag_name == False):
        FunctionIndentLineBreakPrint("\033[3;33mGive this record a name!\033[0;0m")
        FunctionIndentPrint(" - \033[3;33mFor example: (\033[4;36mFood\033[0;0m\033[3;33m - \033[4;32mKFC\033[0;0m\033[3;33m), (\033[4;36mTraffic\033[0;0m\033[3;33m - \033[4;32mbus[215X]\033[0;0m\033[3;33m), (\033[4;36mShopping\033[0;0m\033[3;33m - \033[4;32mSteam\033[0;0m\033[3;33m).\033[0;0m")
        # CSS, the most hated thing in this entire earth, is still better than this crap
        # even brainf*ck is better than this

        name = str(input("\t>> "))

            
        if (name.strip() != ""):        # Check for space-only input: "    "
            if (len(name) > 26):
                FunctionIndentPrint("\033[3;35mUmm...\033[0;0m You can only enter no more than 25 characters here. Sorry!")
                checkflag_name = False

            else:
                checkflag_name = True
                return name

        else:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a number.")
            checkflag_name = False
    




def Record_userInput_Amount():
    checkflag_amount = False

    while(checkflag_amount == False):
        FunctionIndentLineBreakPrint("\033[3;33mHow much is that?\033[0;0m")

        try: 
            amount = input("\t>> $")
            amount_len = len(amount)
            amount = float(amount)
            amount = round(amount, 2)       # round the $ to 2 dec place -> 200.689 -> 200.69


            if (amount_len > 13):
                FunctionIndentPrint("\033[3;35mUmm...\033[0;0m You can only enter no more than 12 numbers here. Sorry!")
                checkflag_amount = False

            else:
                checkflag_amount = True
                return amount
        
        except:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a number.")
            checkflag_amount = False





def Record_userInput_Date():
    checkflag_date = False

    while(checkflag_date == False):
        FunctionIndentLineBreakPrint("\033[3;33mWhen did it happen?\033[0;0m")
        FunctionIndentPrint(" - \033[3;33mIf it happens today, type 'T' or 'Today'.\033[0;0m")
        FunctionIndentPrint(" - \033[3;33mIf it happened in the past, type the date (YYYY-MM-DD) it happens.\033[0;0m")

        date = str(input("\t>> "))

        if (date.upper() == "T" or date.upper() == "TODAY"):
            date = csv_IO.Time_LocalDate()     # Get today date
            checkflag_date = True

            return date

        elif (type(int(date[0])) == int):      
                check_date = date.split("-")    # To find ans split "-" in 2022-11-05     -> Just to avoid someone mis-input the date like 2022/11/05

                if (len(check_date[0]) == 4 and len(check_date[1]) == 2 and len(check_date[2]) == 2 and int(check_date[1]) < 13 and int(check_date[2]) < 32 and int(check_date[0]) > 1969 and int(check_date[1]) > 0 and int(check_date[2]) > 0):
                    # check for length of YYYY, MM, DD and whether MM > 12 or DD > 31
                    checkflag_date = True

                    return date

                else:
                    FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either 'T' / 'Today', or a vaild date (YYYY-MM-DD).")
                    checkflag_date = False
            
        else:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either 'T'/'Today', or a vaild date (YYYY-MM-DD).")
            checkflag_date = False





########################################################################################################
# Update()

def Update_getRowHeader():
    row_header = csv_IO.CSV_getDefaultRowItems()
    row_header[0] = "Date"                  # Remove timestamp (uuid) and replaced with {User entered time}
    del row_header[5]

    return row_header





def Update_getEntries():
    entries = csv_IO.CSV_retrieveEntireListOfEntries()
    if (entries != []):
        del entries[0]                        # delete header
        entries.reverse()                      # To get the latest entries first

        for i in range(0, len(entries)):
            entries[i][0] = entries[i][5]     # replace timestamp with {User entered time}
            del entries[i][5]                  # delete {User entered time}

        return entries

    else:
        return False



def Update_printEntries(row_header, entries):
        # https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

        row_header_format = "\033[1;36m{:>26}\033[0;0m" * (len(row_header))               # {:>20} -> each header takes 20 spaces.  And cyan color
        entries_format = "{:>26}" * (len(entries[0]))

        print("\t\t    ", row_header_format.format(*row_header), sep="")        # * = all elements in the list
                                                                              # \t somehow == 8 spaces here
        print("\t\t", "－" * 67, sep="")                                # 5*(26/2)+2 = 52. +2 because the spaces above "\t    ". 
                                                                                                                 #      ^^^^ 
                                                                      # "－" is full-width character, uses two half-width spaces
        for i in range(0, (len(entries))):
            if (i < 9):                                                                   # To make the (1) and (10) aligned in the table
                print(f"\t\t({i + 1}) ", entries_format.format(*entries[i]), sep="")        # Will be a mess if user entered a long string for category or name

            else:
                if (i % 10 == 0):
                    print("\t\t", "＝" * 67, sep="")
                    
                print(f"\t\t({i + 1})", entries_format.format(*entries[i]), sep="")        

        print("\t\t", "－" * 67, "\n", sep="")





def Update_getEntryNumber(entries_len):
    checkflag = False
    entries_len += 1

    while(checkflag != True):
        try:    # type verification
            FunctionIndentPrint("Enter the number of entry you would like to update.")
            entry_number = int(input("\t>> "))

            # the first two if and elif checks the entered number is between 0 and length of the entire list of entries
            if (entries_len > int(entry_number) and int(entry_number) > 0):        
                checkflag = True
                return int(entry_number)                  

            elif (entry_number.upper() == "EXIT"):
                main.main()                                 # return to main menu

            else:
                EmojiPrint("\t\t:(", "Invaild input. Cannot find the relevant record")
                checkflag = False

        except:
            EmojiPrint("\t\t:(", "Invaild input. You need to enter a number here!")
            checkflag = False





def Update_getIntentedHeader():
    checkflag = False

    while(checkflag != True):
        FunctionIndentLineBreakPrint("Enter the column you would like to update. \033[3;33m(Date, Income, Category, Name, Amount)\033[0;0m")
        entry_column= str(input("\t>> "))

        if (entry_column.upper() in ("DATE", "INCOME", "CATEGORY", "NAME", "AMOUNT")):
            checkflag = True
            return entry_column.upper()
        
        else:
            EmojiPrint("\t\t:(", "Invaild input.")
            checkflag = False
        




def Update_processEntryColumn(entry_column):
            # want use switch...
        if (entry_column == "DATE"):
            edit = Record_userInput_Date()
            csv_index = 5   # index of {user inputed time} in data.csv
            return [edit, csv_index]

        elif(entry_column == "INCOME"):
            edit = Record_userInput_Income()
            csv_index = 1
            return [edit, csv_index]

        elif(entry_column == "CATEGORY"):
            edit = Record_userInput_Category()
            csv_index = 2
            return [edit, csv_index]

        elif(entry_column == "NAME"):
            edit = Record_userInput_Name()
            csv_index = 3
            return [edit, csv_index]

        elif(entry_column == "AMOUNT"):
            edit = Record_userInput_Amount()
            csv_index = 4
            return [edit, csv_index]





########################################################################################################
# Misc

# Basically just some different versions of print()
# Just want to be more organize with the printed string
def IndentPrint(string):
    print("\t", str(string), sep="")

def LineBreakPrint(string):
    print("\n\t", str(string), "\n", sep="")

def EmojiPrint(emoji, string):
    print("\n     ", f"\033[0;31m{emoji}\033[0;0m", " ", str(string), "\n", sep="")

def FunctionIndentPrint(string):
    # For sub-functions e.g. Record(), Update(), View()
    print("\t\t", str(string), sep="")

def FunctionIndentLineBreakPrint(string):
    print("\n\t\t", str(string), sep="")