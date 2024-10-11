from pwn import *


local = True

if local:
    io = process(['python3', 'picker-III.py'])

response = io.recv()
print(response)
io.sendline(b'2')

response = io.recv()
print(response)