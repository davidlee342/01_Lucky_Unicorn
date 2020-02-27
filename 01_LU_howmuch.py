# Lucky Unicorn Decompsition Step 1
# Get initial amount and check it's valid

#Integer checking function
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! please enter an integer between {} " \
                 "and {}" .format(low, high)

        try:
            response = int(input("Enter an integer between {} "
                                 "and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# mian routine gose here

how_mach = intcheck("How much money do you want to play with ", 1, 10)