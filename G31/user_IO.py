# user_IO
# This file contains sub-function of the three major function: Record(), Update(), and View()
# The purpose of this file is to record user's input, process them, and return the result back to main.py

import main
import csv_IO as csv_IO
import datetime

# Record()
########################################################################################################
def Record_userInput():
    """
    Record user's inputs and store them in data.csv

    Input: refer to {CSV_getDefaultColumnItems()} in csv_IO.py 
    Output: a string that contains the record of user income/spending  
    """
    print(" ")
    FunctionIndentPrint("🡫 🡫 🡫")
    FunctionIndentLineBreakPrint("Record your income or spending here!")
    FunctionIndentPrint("Or type '\033[3;34mexit\033[0;0m' and return to the main menu.")


    date      = Record_userInput_Date()
    income    = Record_userInput_Income()
    category  = Record_userInput_Category()
    name      = Record_userInput_Name()
    amount    = Record_userInput_Amount()

    entry = f"{date},{income},{category},{name},{amount}"
    
    return entry





def Record_userInput_Date():
    """
    To get the date of the entry 

    Input: - 
    Output: {date} (string) (in "YYYY-MM-DD" form) -> The date when the event listed in entry occured
    """


    checkflag_date = False

    while(checkflag_date == False):
        FunctionIndentLineBreakPrint("\033[3;33mWhen did it happen?\033[0;0m")
        FunctionIndentPrint(" - \033[3;36mIf it happens today, type 'T' or 'Today'.\033[0;0m")
        FunctionIndentPrint(" - \033[3;36mIf it happened in the past, type the date (YYYY-MM-DD) it happens.\033[0;0m")

        try: 
            date = str(input("\t>> "))

            if (date.upper() == "T" or date.upper() == "TODAY"):
                date = csv_IO.Time_LocalDate()     # Get today date
                checkflag_date = True

                return date


            elif date.upper() == "EXIT":
                main.main()                          # back to main menu


            elif (type(int(date[0])) == int):       # Check whether the first letter in {date} is integer
                    check_date = date.split("-")    # To find ans split "-" in 2022-11-05     -> Just to avoid someone mis-input the date like 2022/11/05

                    if (len(check_date[0]) == 4 and len(check_date[1]) == 2 and len(check_date[2]) == 2 and int(check_date[1]) < 13 and int(check_date[2]) < 32 and int(check_date[0]) > 1969 and int(check_date[1]) > 0 and int(check_date[2]) > 0):
                        # check for length of YYYY, MM, DD and check YYYY > 1969, 0 > MM > 12 and 0 > DD > 31
                        checkflag_date = True

                        return date

                    else:
                        FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either '\033[3;34mT\033[0;0m' or '\033[3;34mToday\033[0;0m', or a vaild date (\033[3;34mYYYY-MM-DD\033[0;0m).")
                        checkflag_date = False
       
        except:
            # should land here if user enter a string
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either '\033[3;34mT\033[0;0m' or '\033[3;34mToday\033[0;0m', or a vaild date (\033[3;34mYYYY-MM-DD\033[0;0m).")
            checkflag_date = False





def Record_userInput_Income():
    """
    To decide whether the entry is income or expense

    Input: - 
    Output:  (boolean) -> True = "income", False = "expense"
    """

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




        else:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter either '\033[3;34mI\033[0;0m' or '\033[3;34mE\033[0;0m'.\n")
            checkflag_income == False





def Record_userInput_Category():
    """
    To get  the category of entry

    Input: - 
    Output: {category} (string) -> The category of the entry
    """

    checkflag_category = False

    while(checkflag_category == False):
        FunctionIndentLineBreakPrint("\033[3;33mWhich category does it belong? (e.g. \033[4;34mFood\033[0;0m\033[3;33m, \033[4;34mTraffic\033[0;0m\033[3;33m, \033[4;34mShopping\033[0;0m\033[3;33m)\033[0;0m")

        category = input("\t>> ")

        try:
            if any(x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for x in category[0].upper()):
                                                                    # https://stackoverflow.com/questions/57062794/how-to-check-if-a-string-has-any-special-characters                    
                                                                    # Return false if number is place before characters. like "6x crab", "7x beer"
                category = category[0].upper() + category[1:]       # Capitalize the first letter of {category}

                if (len(category) > 26):
                    FunctionIndentPrint("\033[3;31mUmm...\033[0;0m You can only enter no more than 25 characters here. Sorry!")
                    checkflag_category = False
            
                else:
                    checkflag_category = True
                    return category

            else:
                FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a word as a category.")
                checkflag_category = False

        except:     # If user enter nothing
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
    """
    To get the name of entry after user entered the category of entry

    Input: - 
    Output: {name} (string) -> The name of the entry
    """
    checkflag_name = False

    while(checkflag_name == False):
        FunctionIndentLineBreakPrint("\033[3;33mGive this record a name!\033[0;0m")
        FunctionIndentPrint(" - \033[3;36mFor example: (\033[4;34mFood\033[0;0m - \033[4;32mKFC\033[0;0m\033[3;36m), (\033[0;0m\033[4;34mTraffic\033[0;0m - \033[4;32mBus[215X]\033[0;0m\033[3;36m), (\033[0;0m\033[4;34mShopping\033[0;0m - \033[4;32mSteam\033[0;0m\033[3;36m).\033[0;0m")
        # CSS, the most hated thing in this entire earth, is still better than this crap
        # even brainf*ck is better than this

        name = str(input("\t>> "))

            
        if (name.strip() != ""):        # Check for space-only input: "    "
            if (len(name) > 26):
                FunctionIndentPrint("\033[3;31mUmm...\033[0;0m You can only enter no more than 25 characters here. Sorry!")
                checkflag_name = False

            else:
                checkflag_name = True
                return name

        else:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a string.")
            checkflag_name = False
    




def Record_userInput_Amount():
    """
    To get the value that user get / spend with their money

    Input: - 
    Output: {amount} (float) -> The amount that the user get from / spend on 
    """

    checkflag_amount = False

    while(checkflag_amount == False):
        FunctionIndentLineBreakPrint("\033[3;33mHow much is that?\033[0;0m")

        try: 
            amount = input("\t>> $")
            amount_len = len(amount)
            amount = float(amount)
            amount = round(amount, 1)       # round the $ to 1 dec place -> 200.69 -> 200.7


            if (amount_len > 13):
                FunctionIndentPrint("\033[3;31mUmm...\033[0;0m You can only enter no more than 12 numbers here. Sorry!")
                checkflag_amount = False

            else:
                checkflag_amount = True
                return amount
        
        except:
            FunctionIndentPrint("\033[1;31m[🗙 ]\033[0;0m Invaild input. Please enter a number.")
            checkflag_amount = False










########################################################################################################
# Update()

def Update_getColumnHeader():
    """
    To get the a list of column header in data.csv

    Input: {column_header} (string) -> A string containing all column headers
    Output : {column_header} (list)  -> A list containing column headers. {User Entered Date} is replaced with {Date}
    """

    column_header = csv_IO.CSV_getDefaultColumnItems()
    column_header = column_header.split(",")
    column_header[0] = "Date"      # Replace "User Entered Date" with "Date"
    return column_header





def Update_getEntries():            # if input {row_data} here, python will also change the content of {row_data}
    """
    To convert data retrieve from data.csv to a list that without column header and in reverse order.

    Input: {entries} (list) -> A list of entries retrieved from data.csv
    Output: {} (list)       -> A list that without column header and in reverse order
    """
    entries = csv_IO.CSV_retrieveEntireListOfEntries()  
    if (entries != []):
        del entries[0]                        # delete header
        entries.reverse()                      # To get the latest entries first

        return entries

    else:
        return False



def Update_printEntries(row_header, entries):
    """
    To print a table of entries in reverse order.
    User can therefore choose easily which entry they want to edit / delete.


    Input: {row_header} (list) -> A list containing strings of header in the list (i.e. "User Entered Date,Income,Category,Name,Amount")
           {entires} (list)    -> A list containing entries that without header and is in reverse order

    Output: -
    """



    # https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
    # Good luck on maintaining it

    row_header_format = "\033[1;36m{:>{date_length}}{:>{income_length}}{:>{category_length}}{:>{name_length}}{:>{amount_length}}\033[0;0m"      # {:>20} -> each header takes 20 spaces.  And cyan color.
    entries_format = "{:>{date_length}}{:>{income_length}}{:>{category_length}}{:>{name_length}}{:>{amount_length}}"     # * by How many column
    
    
    length = []                                     # To get the length of each column
    for j in range(0, len(entries[0])):
        length.append(len(entries[0][j]))           # Get the length of column in the first row

    for i in range(0, len(entries) - 1):
        for k in range(0, len(entries[i])):
            if (len(entries[i][k]) > length[k]):
                length[k] = len(entries[i][k])      # Compare the length of column with other rows



    for i in range(0, (len(entries))):                      # Replace "True" & "False" in Income column with "Income" and "Expense"
        if (entries[i][1].upper() == "TRUE"):
            entries[i][1] = "\033[3;34mIncome\033[0;0m"     # Give "Income" blue color
        
        elif (entries[i][1].upper() == "FALSE"):
            entries[i][1] = "\033[3;33mExpense\033[0;0m"    # Give "Expense" yellow color
        
    for x in range(0, len(length)):
        length[x] = int(length[x]) + 6                     # To add spaces infront of the strings


    income_length = int(length[1]) + 7 + 6       # Compensate for "\033[3;33m" and "\033[0;0m""
                                                        #     ^(len = 7)        ^((len = 6)
                                                        # \033 is 1 character




    # Actual print function
    print("\t\t    ", row_header_format.format(*row_header, date_length = int(length[0]), income_length = int(length[1]), category_length = int(length[2]), name_length = int(length[3]), amount_length = int(length[4])), sep="")      # * = all elements in the list
                                                            # idk but \t == 8 spaces here
    print("\t\t", "－" * int(sum(length) / 2 + 2), sep="")       # +2 because the spaces for print function above,  "\t\t    ". 
                                                                                                                #        ^^^^ 
                                                                    # "－" is full-width character, uses two half-width spaces
    for i in range(0, (len(entries))):
        if (i < 9):                                               # To make the (1) and (10) aligned in the table
            print(f"\t\t({i + 1}) ", entries_format.format(*entries[i], date_length = int(length[0]), income_length = income_length, category_length = int(length[2]), name_length = int(length[3]), amount_length = int(length[4])), sep="")        # Will be a mess if user entered a long string for category or name

        else:
            if (i % 10 == 0):
                print("\t\t", "＝" * int(sum(length) / 2 + 2), sep="")
                
            print(f"\t\t({i + 1})", entries_format.format(*entries[i], date_length = int(length[0]), income_length = income_length, category_length = int(length[2]), name_length = int(length[3]), amount_length = int(length[4])), sep="")        

    print("\t\t", "－" * int(sum(length) / 2 + 2), "\n", sep="")





def Update_getEntryNumber(entries_len):
    """
    To get the number of entry which user want to edit.
    Note that the number is corresponding to the table displayed on the console. Not the index of entries list.
    User can also type "exit" to leave to leave Update()

    Input: {entries_len} (int) -> Provide a restriction and stop user from entering a number that exceed the number of entries in list. 

    Output: {entry_number} (int) / (str) -> A number that is (1 - {index of the entry in list of entries without header})
                                        -> A string which indicates user want to exit this function.

    """ 

    checkflag = False

    while(checkflag != True):
        try:    # type verification
            FunctionIndentPrint("Enter the number of entry you would like to update / delete.")
            FunctionIndentPrint("Or type '\033[3;34mexit\033[0;0m' and return to the main menu.")
            entry_number = input("\t>> ")

            if (entry_number.upper() == "EXIT"):
                main.main()   # return to main menu
                              # again, it's a bad practice but it works really well

            elif (entries_len + 1 > int(entry_number) and int(entry_number) > 0):    #  checks the entered number is between 0 and length of the entire list of entries   
                checkflag = True
                return int(entry_number)  


            else:
                EmojiPrint("\t\t\033[0;31m:(\033[0;0m", "Invaild input. Cannot find the relevant record.")
                checkflag = False

        except:
            EmojiPrint("\t\t\033[0;31m:(\033[0;0m", "Invaild input. You need to enter a number here!")
            checkflag = False





def Update_getIntentedHeader():
    """
    To get which column the user want to edit.
    Or to get user's instruction to delete an entry

    Input: entry_column (string) -> A string that user entered that consists the name of column, or "D" and "Delete"
    Output: The name of the column or "d" and "delete" in capital letter
    """

    checkflag = False

    while(checkflag != True):
        FunctionIndentLineBreakPrint("Enter the column you would like to update. \033[3;33m(Date, Income, Category, Name, Amount)\033[0;0m")
        FunctionIndentPrint("You can also type '\033[3;31mD\033[0;0m' or '\033[3;31mDelete\033[0;0m' to remove an entry.")
        entry_column= str(input("\t>> "))

        if (entry_column.upper() in ("DATE", "INCOME", "CATEGORY", "NAME", "AMOUNT", "D", "DELETE")):
            checkflag = True
            return entry_column.upper()
        
        else:
            EmojiPrint("\t\t\033[0;31m:(\033[0;0m", "Invaild input.")
            checkflag = False
        




def Update_processEntryColumn(entry_column):
    """
    Get the content that user want to edit via the related sub-function in Record()
    Then return the result back to Update()

    Or delete entry that the user entered in Update_getEntryNumber()

    Input: entry_column (string) -> Determind which column user want to edit or the row user want to delete
    Output: 
            either:
                    [edit, csv_index]     
                            edit (string) -> The content that user entered to edit the entry with
                            csv_index (int) -> A number that corresponds to the index of the selected column in the list of entries

                    False (boolean) -> Just a value that isn't list. Return "False" if the user decide to delete the row of entry  
    """


    # want to use switch...
    if (entry_column == "DATE"):
        edit = Record_userInput_Date()
        csv_index = 0                   # index of {user inputed date} in data.csv
        return [edit, csv_index]

    elif (entry_column == "INCOME"):
        edit = Record_userInput_Income()
        csv_index = 1
        return [str(edit), csv_index]

    elif (entry_column == "CATEGORY"):
        edit = Record_userInput_Category()
        csv_index = 2
        return [edit, csv_index]

    elif (entry_column == "NAME"):
        edit = Record_userInput_Name()
        csv_index = 3
        return [edit, csv_index]

    elif (entry_column == "AMOUNT"):
        edit = Record_userInput_Amount()
        csv_index = 4
        return [str(edit), csv_index]

    elif (entry_column == "D" or entry_column == "DELETE"):
        return False










########################################################################################################
# View

def View_getCurrentBalance(indent):
    """
    Calculate the overall balance with all records in data.csv

    input: indent (boolean) -> Print the result with indentation if {indent} == True
    output: -  
    """

    entries = csv_IO.CSV_retrieveEntireListOfEntries()

    income_entries = [row for row in entries if row[1].upper() == "TRUE"]       # Put the income entries in a list
    expense_entries = [row for row in entries if row[1].upper() == "FALSE"]     # Same as above but expense

    income_value_list = [float(column[4]) for column in income_entries]         # Put the value in income entries in a list
    expense_value_list = [float(column[4]) for column in expense_entries]

    balance =  round(sum(income_value_list) - sum(expense_value_list), 1)       # avoid floating point error


    # Give some color to balance
    if (indent == True):        # Have indentation, basically for View() only
        if (balance > 0):
            FunctionIndentLineBreakPrint(f"Current balance: \033[1;42m {balance} \033[0;0m\n")

        elif (balance == 0):
            FunctionIndentLineBreakPrint(f"Current balance: \033[1;43m {balance} \033[0;0m\n")

        elif (balance < 0):
            FunctionIndentLineBreakPrint(f"Current balance: \033[1;41m {balance} \033[0;0m\n")

    else:
        if (balance > 0):
            IndentPrint(f"Current balance: \033[1;42m {balance} \033[0;0m\n")

        elif (balance == 0):
            IndentPrint(f"Current balance: \033[1;43m {balance} \033[0;0m\n")

        elif (balance < 0):
            IndentPrint(f"Current balance: \033[1;41m {balance} \033[0;0m\n")





# Part 3
def GoodSort(value):
    return (sorted(value, key = lambda x: x[4], reverse = True))
 
def Top_ThreeSpendings(days_numbers):
    """
    Printing the top three spendings in the last 30 days

    input: -
    output: -
    """
    entries = csv_IO.CSV_retrieveEntireListOfEntries()
    expense_entries = [row for row in entries if row[1].upper() == "FALSE"]
    date_delta = RetriveTargetdate(days_numbers)
                                   
    expense_entries_in_30_days = []
 
    # Filitering rows of last 30 days
    for row in expense_entries:
        current_date = row[0].split("-")
        current_date = datetime.date(int(current_date[0]),int(current_date[1]),int(current_date[2]))
 
        if current_date > date_delta :
            expense_entries_in_30_days.append(row)
 
    expense_entries_in_30_days = GoodSort(expense_entries_in_30_days)
    # https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
    edge_number = 0
    i = 0
    end_number = 0
    while i != 3 :
        repeat = True
        while repeat :
            if expense_entries_in_30_days[end_number+1][4] != expense_entries_in_30_days[end_number][4]:
                repeat = False
                end_number = end_number + 1
                i = i + 1
            else:
                end_number = end_number + 1

    entries_to_print =[]
    for i in range(0, end_number):
        entries_to_print.append(expense_entries_in_30_days[i])

    column_header = Update_getColumnHeader()
    print("")   # line break 
    Update_printEntries(column_header , entries_to_print)

def RetriveTargetdate(days_numbers):                                            # Finding the date 30 days before
    date0 = datetime.date.today()
    days_numbers = datetime.timedelta(days_numbers)
    Target_date = date0 - days_numbers
    return Target_date




# Part 4
def View_getBalanceOfEachCategory():
    # Monthly Balance (code that scraped but I think it's kinda cool)
    # https://pastebin.com/HAU6kJXV 

    """
    To print the sum of each category and the overall balance in format of financial statement

    Input: {entries} (list) -> A list from data.csv that removed the column headers and in reverse order
    Output: -

    """

    list_1 =  View_getSortedCategoryList()
    income_sorted_by_category = list_1[0]
    income_value = list_1[1]
    expense_sorted_by_category = list_1[2]
    expense_value = list_1[3]

    # print part
    #can use "os.get_terminal_size()" to make the content responsive 

    income_string = "\033[4;34mIncome\033[0;0m"
    expense_string = "\033[4;33mExpense\033[0;0m"

    table_width = 60
    line_width = 12


    # print category in income
    print(f"\n\t\t{income_string: <{table_width + 13}}\n")     # 13 -> len(\033[4;34m) = 7, len(\033[0;0m) = 6 
    for key in income_sorted_by_category:
        for i in range(0, len(income_sorted_by_category)):
            income_value[key].append(float(income_sorted_by_category[key][i][4]))   # Don't know why there are list in list but whatever
        income_value[key] = round(sum(income_value[key]), 1)    # avoid floating point error
        FunctionIndentPrint(f"{key}{income_value[key]: >{table_width - len(key)}}")
    print("\t\t", " " * (table_width - line_width), "-" * line_width, sep="")
    print("\t\t", " " * (table_width-len(str(sum(income_value.values())))), f"\033[0;34m{sum(income_value.values())}\033[0;0m", sep="")
    



    # print category in expense
    print(f"\t\t{expense_string: <{table_width + 13}}\n")
    for key in expense_sorted_by_category:
        for j in range(0, len(expense_sorted_by_category[key])):
            expense_value[key].append(float(expense_sorted_by_category[key][j][4]))
        expense_value[key] = round(sum(expense_value[key]), 1)
        FunctionIndentPrint(f"{key}{expense_value[key]: >{table_width - len(key)}}")
    print("\t\t", " " * (table_width - line_width), "-" * line_width, sep="")
    print("\t\t", " " * (table_width-len(str(sum(expense_value.values())))), f"\033[0;33m{sum(expense_value.values())}\033[0;0m", sep="")
    print("\t\t", " " * (table_width - line_width), "-" * line_width, sep="")



    # print balance
    balance = sum(income_value.values()) - sum(expense_value.values())
    if (balance > 0):
        print("\t\t", " " * (table_width - len(str(balance))), f"\033[1;32m{balance}\033[0;0m", sep="")

    elif (balance == 0):
        print("\t\t", " " * (table_width - len(str(balance))), f"\033[1;33m{balance}\033[0;0m", sep="")

    elif (balance < 0):
        print("\t\t", " " * (table_width - len(str(balance))), f"\033[1;31m{balance}\033[0;0m", sep="")

    print("\t\t", " " * (table_width - line_width), "=" * line_width, "\n", sep="")

    
    


def View_getSortedCategoryList():

    """
    To print the sum of each category and the overall balance in format of financial statement

    Input: {entries} (list) -> A list from data.csv that removed the column headers and in reverse order
    Output: -

    """

    entries = Update_getEntries()
    
    category_list = list(set([x[2] for x in entries]))        # get a list of category without duplicates  
                                                               # https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists 
    income_sorted_by_category = {}
    income_value = {}
    expense_sorted_by_category = {}
    expense_value = {}

    # process entries
    for row in entries:
        if row[2] not in income_sorted_by_category or expense_sorted_by_category:        # Initialize key before append value
            income_sorted_by_category[row[2]] = []                                        # https://stackoverflow.com/questions/41970992/appending-values-to-dictionary-in-for-loop
            income_value[row[2]] = []                      # Should have same structure with above 
            expense_sorted_by_category[row[2]] = []
            expense_value[row[2]] = [] 

    for row in entries:                                                                  # Append value to keys
        #if row[2] in category_list:
            if (str(row[1]).upper() == "TRUE"):
                income_sorted_by_category[row[2]].append(row)                           
            
            elif (str(row[1]).upper() == "FALSE"):
                expense_sorted_by_category[row[2]].append(row)
    

    for key in list(income_sorted_by_category) and list(expense_sorted_by_category):    # Delete unused keys
        if income_sorted_by_category[key] == []:                                        # https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error
            del income_sorted_by_category[key]
            del income_value[key]                   # Too lazy to write code to vaildate this 
    
        elif expense_sorted_by_category[key] == []:
            del expense_sorted_by_category[key]
            del expense_value[key]


    return [income_sorted_by_category, income_value, expense_sorted_by_category, expense_value, category_list]

    



def View_printCategoryRecords():
    list_1 =  View_getSortedCategoryList()

    income_sorted_by_category = list_1[0]
    expense_sorted_by_category = list_1[2]
    category_list = list_1[4]

    list_of_that_category = []

    FunctionIndentLineBreakPrint("Please enter the category you would like to view.")
    FunctionIndentPrint(f"\033[3;33m({(', '.join(sorted(category_list)))})\033[0;0m")
    category = input("\t>> ")

    for key in income_sorted_by_category:
        if (key.upper() == category.upper()):
            for i in range(0, len(income_sorted_by_category[key])):
                list_of_that_category.append(income_sorted_by_category[key][i])

    for key in expense_sorted_by_category:
        if (key.upper() == category.upper()):
            for i in range(0, len(expense_sorted_by_category[key])):
                list_of_that_category.append(expense_sorted_by_category[key][i])

    column_header = Update_getColumnHeader()
    print("")   # line break 
    Update_printEntries(column_header , list_of_that_category)

########################################################################################################
# Misc

# Basically just some different versions of print()
# Just want to be more organize with the printed string
def IndentPrint(string):
    print("\t", str(string), sep="")

def LineBreakPrint(string):
    print("\n\t", str(string), "\n", sep="")

def EmojiPrint(emoji, string):
    print("\n     ", f"{emoji}", " ", str(string), "\n", sep="")

def FunctionIndentPrint(string):
    # For sub-functions e.g. Record(), Update(), View()
    print("\t\t", str(string), sep="")

def FunctionIndentLineBreakPrint(string):
    print("\n\t\t", str(string), sep="")
