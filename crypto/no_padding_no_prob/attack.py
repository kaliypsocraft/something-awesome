from pwn import *

host = 'mercury.picoctf.net'
port = 33780
io = remote(host, port)

recvuntil()
