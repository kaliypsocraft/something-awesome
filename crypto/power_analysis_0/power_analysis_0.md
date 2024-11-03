# CTF Write-Up: [Power Analysis][Cryptography]

## Description
>This encryption algorithm leaks a "bit" of data every time it does a computation. Use this to figure out the encryption key.
## Flag
`picoCTF{example_flag}`

## Difficulty
- **Difficulty Level:** [easy/medium/hard]

## Tools Used
- pwntools
- 
## Write-Up

### Preparatory Phase

The `leaky_aes_secret` function is of interest to us. It appears to conduct a bitwise xor with a plain-text byte and a key byte. It then uses the result from this as the index of the `SBox` or our substitution box. It then appends whether the last-bit of the output is set or not via bit-wise and operator.
```py
leak_buf = []
def leaky_aes_secret(data_byte, key_byte):
    out = Sbox[data_byte ^ key_byte]
    leak_buf.append(out & 0x01)
    return out
```

The user it then provided the number of 1's present in the `leak_buf` list.
```py
def encrypt_and_leak(plaintext):
    ciphertext = encrypt(plaintext, SECRET_KEY)
    ciphertext = None # throw away result
    time.sleep(0.01)
    return leak_buf.count(1)

```

### Attack Phase
- Using the prep from above, walking through the steps taken to conduct a successful attack
### Final Solution/Payload
- If a payload was used place into here, otherwise use screenshot of the flag

### Lessons Learnt
- **List comprehensions in python**

```py 
ciphertext = [leaky_aes_secret(plaintext[i], key[i]) for i in range(16)]
```
This is equivalent to 
```py
for i in range(16):
    ciphertext[i] = leaky_aes_secret(plaintext[i], key[i])

```
- **What are side-channel attacks**


- **What is a power analysis attack**
## References
- TODO: Ensure these go into the `SUBMISSION_REPORT.md`

