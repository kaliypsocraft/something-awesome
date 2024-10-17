from pwn import *

io = process('./out')

password = b'7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f35646565343434317d'
io.sendline(password)
resp = io.recvall()
print(resp)