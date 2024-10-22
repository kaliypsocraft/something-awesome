from pwn import *

host = 'titan.picoctf.net'
port = 65045

io = remote(host, port)
payload = b'qezjdvjltvuxavgiibmkrsncqrntxfykgmntwsepmyvyguzwtv'

io.sendline(payload)
resp = io.recvall()
print(resp)