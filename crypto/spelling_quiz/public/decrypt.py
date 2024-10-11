english_freq = [
    'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r',
    'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y',
    'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z'
]

cipher_freq = [
    'e', 'o', 'i', 'b', 'j', 'e', 'g', 'z', 'd', 
    'h', 'r', 'x', 'k', 'm', 'l', 't', 'y', 'a', 
    'u', 'n', 'f', 'v', 'p', 's', 'w', 'q'
]
dictionary = dict(zip(cipher_freq, english_freq))
text = open('study-guide.txt', 'r').read()
# if c is in the dictionary substitute it
# otherwise use the identity map i.e. if _ or punctuation
decrypted = ''.join([
    dictionary[c]
    if c in dictionary else c
    for c in text
])
open('output.txt', 'w').write(decrypted)

