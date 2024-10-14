from pwn import *
from Cryptodome.Util.number import long_to_bytes
from sage.all import *

host = 'mercury.picoctf.net'
port = 33780
io = remote(host, port)

resp = io.recvuntil(b'e:')
n = int(resp.strip().split()[-2].decode())
print(f"n: {n}")
resp = io.recvuntil(b'ciphertext:')
e = int(resp.strip().split()[0].decode())
print(f"e: {e}")
resp = io.recvuntil(b'Give me')
c = int(resp.strip().split()[0].decode())
print(f"c: {c}")

payload_1 = 2*c
io.sendline(str(payload_1).encode())
resp = io.recvline()
numerator = int(resp.strip().split()[-1].decode())

payload_2 = 2
io.sendline(str(payload_2).encode())
resp = io.recvline()
denom = int(resp.strip().split()[-1].decode())

denom_inverse = pow(denom, -1, n)
plain_text_in_bytes = (numerator * denom_inverse) % n
print(f"Flag: {long_to_bytes(plain_text_in_bytes)}")