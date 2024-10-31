# CTF Write-Up: [Challenge Name][Challenge Type]

## Description
>A brief description of the challenge, including its title, type (e.g., web, crypto, pwn)


## Flag
The flag you obtained after solving the challenge. (e.g., `picoCTF{example_flag}`)

## Difficulty
- **Difficulty Level:** [easy/medium/hard]

## Tools Used
- List any tools or resources you used to solve the challenge (e.g., Wireshark, Burp Suite, Python, etc.).

## Write-Up

### Preparatory Phase
The code analysis reveals that values $p$ and $g$ are hard-coded as $97$ and $31$ respectively. These values are input into a generator function, which calculates values $u$ and $v$. In this generator function:

- $u$ is computed as $g^{a} \mod p$
- $v$ as $g^{b} \mod p$, where $a$ and $b$ are values likely representing private keys or random values.

The `key` value in the code is calculated as $v^{a} \mod p$, while `b_key` is computed as $u^{b} \mod p$. These values represent shared secrets, which are typically derived from Diffie-Hellman key exchange, where both parties can independently compute a shared secret without directly sharing private keys.

A function named `dynamic_xor_encrypt(plain_text, text_key)` is present in the code, with the string `trudeau` hardcoded as `text_key`. The encryption function operates by iterating over the reversed version of the plain text, performing a dynamic XOR operation. Specifically, each character of the reversed plain text is XORed with a character from the `text_key` at a position determined by i % key_length, where $i$ is the current index in the reversed plain text. This results in a partially encrypted output, or "semi-cipher."

Following this, the cipher text (now "semi_cipher") is fed into an `encrypt(semi_cipher, shared_key)` function. Within this function, each ASCII value of a character in the semi-cipher is multiplied by the product of `key` and $311$. This final transformation further modifies the semi-cipher based on the shared secret key, incorporating an additional multiplication factor.


### Attack Phase
- First, obtain the `key` value, multiply it by $311$, and divide by each value in the array to generate the initial decrypted values.

- Then, XOR the `key` with `text_key[i \% \text{key_length}]` to reconstruct the reversed plain text.

- Finally, reverse the plain text to retrieve the original message.
### Final Solution/Payload
```py
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
```

### Lessons Learnt
Although the problem was straight-forward in simply reverse engineering the encryption process. It did require a level of attention to detail in order to not miss a vital step. 
## References
- Link to any external resources, write-ups, or documentation that were helpful in solving the challenge.

