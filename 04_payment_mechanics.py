# Lucky Unicorn - payment mechanics

# To do
# Adjust total correctly for a given token
#   - if it's a unicorn, add $5
#   - if it's a zebra \ hores, subtract 0.5
#   - if it's a donkey, subtract 1
# Give user feedback based on winnings...
# state new total

# Assume starting amount is $10
total = 10

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
print("you have {} to play with".format(total)).
