def get_num(prompt):
    """Makes the user enter a float value in response to a prompt.
       Includes error checking to ensure a valid input is entered.
    Args:
        numF: The inputed number that can be a float
    Returns:
        numF: A float number
    """
    validInput=False
    while not validInput:
        try:
            numF=float(input(prompt))
            validInput=True
        except:
            print("Please enter a number")
    return numF

def get_int(prompt):
    """Makes the user enter a integer value in response to a prompt.
       Includes error checking to ensure a valid input is entered.
    Args:
        numI: The inputed number that can must be an integer
    Returns:
        numI: An integer number
    """
    validInput=False
    while not validInput:
        try:
            numI=int(input(prompt))
            validInput=True
        except:
            print("Please enter an integer")
    return numI

def get_float(prompt):
    """Makes the user enter a integer value in response to a prompt.
       Includes error checking to ensure a valid input is entered.
    Args:
        numI: The inputed number that can must be an integer
    Returns:
        numI: An integer number
    """
    validInput=False
    while not validInput:
        try:
            numI=float(input(prompt))
            validInput=True
        except:
            print("Please enter a numerical value.")
    return numI
def get_positive_int(flag, prompt):
    """Makes the user enter a postive integer while considering 0 as a valid input
       depending on the flag variable. Includes error checking to ensure a valid
       input is entered.
    Args:
        flag(boolean): Whether or not 0 will be considered an acceptable input
                       for this function.
        prompt(string): The question/prompt that precedes the users input.
    Returns:
        numPI: A postive integer value inputted by the user that can potentially
               be 0.
    """
    validInput=False
    while not validInput:
        try:
            numPI=int(input(prompt))
            if flag:
                if numPI>=0:
                    return numPI
                else:
                    10 / 0
            elif not flag:
                if numPI>0:
                    return numPI
                else:
                    10 / 0
        except:
            print("Please enter an positive integer")   
def get_option(n, prompt):
    """Has the user input an integer from 1 to n. Also asked a prompt prior to
       entering an input. Includes error checking to ensure a valid input is
       entered.
    Args:
        n(integer): The number that the options go up till.
        prompt(string): The question/prompt that precedes the users input
    Returns:
        numPI: A postive integer value inputted by the user that can potentially
               be 0.
    """
    validInput=False
    while not validInput:
        try:
            option=int(input(prompt))
            if option>=1 and option<=n:
                return option
            else:
                print("Please enter a input.") 
                continue
        except:
            print("Please enter an option")   
def main():
#get_num() test cases
    for test in ["Enter a number","Enter a float"]:     #Output must be float
        print(get_num(test))                            #<class 'float'>
        
#get_int() test cases
    for test in ["Enter a int","Enter an integer"]:    #Output must be int
        print(get_int(test))                              #<class 'int'>

#get_positive_int() test cases
    #Output must be int greater than 1, the first accepts 0 while the next doesn't
    for flag,prompt  in [[True,"Enter a postive integer"], [False,"Positive Integer:"]]:
        print(get_positive_int(flag,prompt))                      #<class 'int'>
#get_option() test cases
    #Output must be int from 1 to n
    for n,prompt in [[2,"Pick an option (1-2)"],[ 21,"Option (1-21):"]]:     
        print(get_option(n, prompt))                    #<class 'int'>
if __name__ == '__main__':
    main()