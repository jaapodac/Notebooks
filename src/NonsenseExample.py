# John Apodaca
# August 27 2017

# Attempt1.py

# Reacquainting myself with a language that used to be  in a children's
# category along with the likes of LOGO.

#Note: You need to restart the shell after you edit a file before you
# load the file.
# 1. Save your *.py file in the Editor
# 2. From the IDLE menus, Shell -> Restart Shell
# 3. In IDLE Shell command line, >>> import attempt1
# 4. In IDLE Shell command line, attempt1.FibbonacciNumbers(100)

#Extra Notes
# Use Alt-P to repeat the last command
# Place the cursor on the line you want to repeat, hit Enter

# To view the funtion list inside your *.py file use dir(attempt1)

# Phython functions can be very powerful e.g. variable arguments!
# https://www.codementor.io/kaushikpal/user-defined-functions-in-python-8s7wyc8k2
# also
# to create packages...
# https://learn.adafruit.com/micropython-basics-loading-modules/import-code

import sys

def FibbonacciNumbers(howMany = 1000):
    """This is a documentation string.This function produces a series of
    numbers up to howMany."""
    a, b = 0, 1
    count = 1
    while b < howMany:
            print(b, end=',')
            a, b = b, a+b
            count = count + 1
    print(" Produced this many numbers: ", count)
    return;

def SquareList( userList = []):
    """This function takes List input and squares each element as output.
    The default list is Null which generates an error for the user to
    correct.
    """
    
    if userList == []:
        print("Empty or Null List in Argument.")
        sys.exit()
    newList = []
    howBig = len(userList)

    for i in range (0, howBig):
        newList.append(userList[i]**2)

    return newList;

def Combinatorics():
    """With almost no effort, you can perform brute force combinatorics."""

    print([(x, y) for x in ["a","c","e"] for y in ["b","d","f"] if x != y])
    print("Here are all possible combinations without repeats.")
    #No return statement when there are no parameters.
    
