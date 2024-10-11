import random
import os
import pprint

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]


alphabet = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(shuffled := alphabet[:])
dictionary = dict(zip(alphabet, shuffled))

pprint.pprint(dictionary)

for filename in files:
    text = open(filename, 'r').read()
    # if c is in the dictionary substitute it
    # otherwise use the identity map i.e. if _ or punctuation
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename, 'w').write(encrypted)
