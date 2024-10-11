#!/usr/bin/python3
import re

frequencies = {}

with open('message.txt', 'r') as file:
    for line in file:
        for letter in line:
            letter = letter.lower()
            if letter not in frequencies:
                frequencies[letter] = 1
            else:
                frequencies[letter] += 1
sorted_items = sorted(frequencies.items(), key=lambda item: item[1])  

with open('message.txt', 'r') as file:
    file_contents = file.read()
    
file_contents = re.sub(r'f', 'e', file_contents, flags=re.IGNORECASE)
file_contents = re.sub(r's', 'p', file_contents, flags=re.IGNORECASE)       
file_contents = re.sub(r'x', 'i', file_contents, flags=re.IGNORECASE)
file_contents = re.sub(r'z', 'c', file_contents, flags=re.IGNORECASE)
file_contents = re.sub(r'q', 'o', file_contents, flags=re.IGNORECASE)
file_contents = re.sub(r'n', 't', file_contents, flags=re.IGNORECASE)    
file_contents = re.sub(r'v', 'f', file_contents, flags=re.IGNORECASE)
file_contents = re.sub(r'u', 'v', file_contents, flags=re.IGNORECASE)

with open('decryption2.txt', 'w') as file:
    file.write(file_contents)