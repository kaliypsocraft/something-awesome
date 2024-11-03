from pwn import *

host = 'saturn.picoctf.net'
port = 63491

plaintext = b'A'*32
io = remote(host, port)
io.sendline(plaintext)
resp = io.recvall()
print(resp)