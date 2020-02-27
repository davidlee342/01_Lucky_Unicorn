# Lucky Unicorn Decomposition step 2
# Generate a random token

# to do
# set up starting amount
# Choose 100 tokens  (ie: play 100 rounds and...
#    count # of unicorns and multiply by 5
#    count # of hores / zebera and multiply by 0.5
#    count # of donkeys
#    work out total won / lost

import random

HOW_MUCH = 100
tokens = ["horse", "zebra", "donkey", "unicorn"]

Unicorn_count = 0
zebhor_count = 0
donkey_count = 0

for item in range(1,HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1
    print(chosen)

