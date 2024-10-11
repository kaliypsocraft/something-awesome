import math
import pprint

def generator(g, x, p):
    return pow(g, x) % p

p = 97
g = 31
a = 97
b = 22

u = generator(g, a, p)
v = generator(g, b, p)
key = generator(v, a, p)
b_key = generator(u, b, p)


def decrypt(cipher_text, text_key):
    plain_text = ""
    key_length = len(text_key)
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_char = chr(char ^ ord(key_char))
        plain_text += decrypted_char
    return plain_text

def semi_decrypt(cipher_text, key):
    semi_plain = []
    for char in cipher_text:
        semi_plain.append(char // (key*311))
    return semi_plain

shared_key = key    

print(shared_key * 311)
cipher = [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]
semi_decryption = semi_decrypt(cipher, shared_key)

# pprint.pprint(semi_decryption)

plain_text = ''.join(reversed(decrypt(semi_decryption, "trudeau")))

print(plain_text)