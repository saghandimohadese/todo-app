1
import functions.py

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)


functions.py:

def count(phrase):
return phrase.count('.')
