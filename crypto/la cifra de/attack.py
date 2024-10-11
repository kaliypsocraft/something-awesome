import re
import pprint


dictionary = {}

with open('cipher.txt', 'r') as file:
    for line in file:
        for letter in line:
            if not letter.isalpha():
                continue
            if letter.capitalize() not in dictionary:
                dictionary[letter.capitalize()] = 1
            else:
                dictionary[letter.capitalize()] += 1
pprint.pprint(dictionary)