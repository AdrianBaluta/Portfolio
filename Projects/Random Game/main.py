import random
import sys

sys.argv

input({'Please guess a number between 1 and 10'})

random.randint(1,10)

x = random.randint(1,10)

y = random.choice([1, 10])


if x == y:
    print({'You are a genius'})

else:
    while x != y:
        print({'Please try again'})
        input({'Please guess a number between 1 and 10'})
