# Lucky Unicorn - payment mechanics

#To do
# ask user how much money they have to play with
# If the total is less than $1, qiut
# If the tolat is more than $1, ask user if they want to keep going


# assume starting amount is $10
total = int(input("How mach would you like to play with? "))

keep_going = ""
while keep_going == "":

  # Allow manual token input for testing purposes
  token = input("enter a token: ")

  # Adjust total correctly for a given token
  if token == "unicorn:":
      total += 5
      feedback = "congratulations you won $5.00"
  elif token == "donkey":
      total -= 1
      feedback = "sorry, you did not win anything this round "
  else:
     total -= 0.5
     feedback = "congratulations you won 50c"

  print()

  print(feedback)
  print("you have {} to play with".format(total))

  if total < 1:
      print("sorry you don't have enough money to continue.  Game over")
      keep_going = "end"
  else:
      keep_going = input("press <enter> to play again or any key to quit")

print("Thank you for playing.")