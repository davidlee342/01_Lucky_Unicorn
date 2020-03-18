# Lucky Unicorn Fully Workering program
# progaram should work - needs  to be teated for usability

import random


#Integer checking function below
def intcheck(question, low, high):
      valid = False
      error = "Whoops! please enter an integer between {} " "and {}" .format(low, high)
      while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


def statement_generator(statement, char):
    print(len(statement) * char)
    print(statement)
    print(len(statement) * char)
    return ""

# Main routine



# ask user how much they want to play with  (min $1, max $10)
balance = intcheck("How much money do you want to play with ", 1, 10)

keep_going = ""
while keep_going == "":

    # tokens list includes 10 items to prevent too many unicorns being chosen
    tokens =[ "horse","horse","horse",
              "zebra","zebra","zebra",
              "donkey","donkey","donkey","unicorn"]

    # Randomly choose a token form our list above
    token = random.choice(tokens)

    # Adjust total correctly for a given token
    if token == "unicorn:":
        balance += 5
        feedback = "*** Congratulations you got a unicorn and won $5.00 ****"
        decoration = "*"
    elif token == "donkey":
        balance -= 1
        feedback = "!!! Sorry, you got a donkey and did not win anything this round !!!"
        decoration = "!"
    else:
        balance -= 0.5
        feedback = "^^^ Congratulations you got a {} and won 50c ^^^".format(token)
        decoration = "^"

    print()

    statement_generator(feedback, decoration)
    print()

    print("you have ${:.2f} to play with".format(balance))
    if balance < 1:
        print("sorry you don't have enough money to continue.  Game over")
        keep_going = "end"
    else:
        keep_going = input("press <enter> to play again or any key to quit")

print("Thank you for playing.")