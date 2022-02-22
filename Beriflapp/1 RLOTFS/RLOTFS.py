# Read lines of text from STDIN.


def Beriflapp():
    while True:
        # Reading the input from the user
        i = input("What is the value of 2+8 = ")
        # Only exits when meets the condition
        if i == '10':
            break
        print("The value", i, "is the wrong answer. Try again")
    print("The value", i, "is the right answer")
    while True:
        # Reading the input from the user
        i = input("What is the value of 4+1 = ")
        # Only exits when meets the condition
        if i == '5':
            break
        print("The value", i, "is the wrong answer. Try again")
    print("The value", i, "is the right answer")
Beriflapp()