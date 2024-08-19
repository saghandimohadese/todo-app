# import functions
#
# nr_of_periods = functions.count("Trees are good. Grass is green.")
# print(nr_of_periods)


# from functions import count
#
# nr_of_periods = count("Trees are good. Grass is green.")
# print(nr_of_periods)

from parsers import parse
import random


user_input = input("Enter a lower bound and an upper bound separated by a comma (e.g., 2,10): ")


parsed = parse(user_input)

rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)
