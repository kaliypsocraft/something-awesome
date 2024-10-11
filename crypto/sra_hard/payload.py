from pwn import *
import math
from Cryptodome.Util.number import bytes_to_long, long_to_bytes

host = 'saturn.picoctf.net'
port = 59314

local = True

if not local:
    io = remote(host, port)
else:
    io = process(['python3', 'chal.py'])
# anger is the cipher-text
# envy is the decryption exponent
response = io.recv().strip().split()
cipher = int(response[2])
d = int(response[5])
e = 65537

print(f"Response: {response}")
print(f"Cipher: {cipher} | d = {d}")

tentative_phi = (e * d) - 1
print(f"GCD {math.gcd(e, tentative_phi)}")
tentative_message = pow(cipher, d, tentative_phi)
print(long_to_bytes(tentative_message).decode())

print(f" Message: {tentative_message}")
io.sendline(long_to_bytes(tentative_message).decode())

# we can keep dividing until gcd()