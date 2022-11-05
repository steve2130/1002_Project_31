# main.py

import Expense_tracker_data_IO as data_IO

def main():
    """
        Hello! This expense tracker helps you to keep track of your incomes and expenses.
        How can I help you?
    """
    print(main.__doc__)
    while(1):               # Just to loop infinitely
        menu_print()
        
        # Error exception.
        # To check whether the user entered a number or a string
        # throw an error text if user entered a string
        try:        
            option = int(input(">> "))

        except:
            print("\n     :( Please check your entered option. It should be a number between 1 and 3.\n")


        if option == 1:
            View()
        elif option == 2:
            option_2()
        elif option == 3:
            option_3()
        else:
            print("\n     :( Please check your entered option. It should be a number between 1 and 3.\n")





def menu_print():
    """Just to provide a space to quickly edit options' order and text in the menu"""
    # https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
    
    menu_options = {
        1: "View",
        2: "Record",
        3: "Update"
    }

    for key in menu_options.keys():
        print("\t", key, " － ", menu_options[key], sep = "")  # sep is needed so I can use \t 

    print(" ")  # Just to give a line break / <br/>





def View():
    
    if (data_IO.csv_checkFileExistence() == True):
        print("\tPlease enter ")

    else:
        print("\n     :( Cannot find the data file.")
        print("\tWould you like to create a new data file? (Y / N)\n")

        checkflag = False

        while (checkflag == False):                                 # To loop this part if the user entered char != Y / N
            option = input(">> ")

            if option.upper() == "Y" or option.upper() == "YES":
                checkflag = True                                        
                data_IO.csv_creation()
                print("\tData file created!", end="\n")

            elif option.upper() ==  "N" or option.upper() == "NO":
                checkflag = True
                print(" ")  # line break
                return      # go back to menu

            else:
                print("\n     :( Please check you have entered. It should be a character of either Y or N\n")








if __name__ == "__main__":
    main()