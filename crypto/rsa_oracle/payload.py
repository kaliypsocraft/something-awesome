#!/usr/bin/env python3

from Crypto.Util import *
from pwn import *
from gmpy2 import *

host = 'titan.picoctf.net'
port = 56781

io = remote(host, port)
io.recv()
io.sendline(b'E')
io.recv()
io.sendline(b'\x02')

# 2^e mod n
line = io.recv()
print(line)
c_1 = line.strip().split()[13]
x_1 = c_1.decode()

c_2 = open("password.enc", "r")
x_2 = c_2.readline()

x = int(x_1) * int(x_2)
io.sendline(b'D')
io.recv()
io.sendline(str(x))
io.recvuntil('hex (c ^ d mod n):')

# This is 2*m
m_2 = int(io.recvline().decode(), 16)
print(bytes.fromhex(hex(m_2 // 2)[2:]).decode('utf-8'))


