# CTF Write-Up: [No Padding No Problem][Cryptography]

## Description
![image](https://github.com/user-attachments/assets/edddecf1-25d6-40b2-bd55-1804b2247ccc)
The user is provided an oracle which decrypts cipher-texts. This indicates a chosen-cipher text attack. 
## Flag
The flag you obtained after solving the challenge. (e.g., `picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_0801973}`)

## Difficulty
- **Difficulty Level:** [medium]

## Tools Used
- pwntools (Remote-connection)
- Cryptodome (convert between long and byte formats)

## Write-Up

### Step 1: [Prepartory Phase]
- Assuming generic RSA algorithm (namely it is deterministic)
- Assuming it requires a chosen-cipher text attack since we are provided a decryption oracle
- We are given $e$, $n$, $c$ upon remotely connecting to the server.

  ![image](https://github.com/user-attachments/assets/afe63041-43bf-4636-bdaf-5d8cee6ce86c)

  
### Step 2: [Attack Phase]
Consider the following scenario, where $d$ is the RSA private-key and $m$ is the flag. In order to obtain
the flag we need to obtain $c^{d} \mod n$. 
- Since we cannot query the cipher-text $c$ directly
- I will take advantage of the algebraic properties of RSA and the deterministic nature of textbook RSA.
We can query $2 \times c$ to the oracle to obtain $c_1 = (2c)^{d} \mod n$. We the query $2$ to the oracle to obtain $c_2 = 2^{d} \mod n$.
With these two decryptions we can obtain $m$ by the following: $$= \frac{(2c)^{d} \mod n}{2^{d} \mod n}$$ $$= \frac{2^{d}c^{d} \mod n}{2^{d} \mod n}$$
$$= c^{d} \mod n$$
$$= m$$

### Final Solution/Payload
```python
from pwn import *
from Cryptodome.Util.number import long_to_bytes

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

```

## Lessons Learned
- Be careful when conducting division when dealing with moduli. It is non-trivial to not consider the moduli when dividing two numbers.
- Do not overthink the decoding of a big integer, usually `Cryptodome.Util.numbers.long_to_bytes()` does the trick.
## References
- Link to any external resources, write-ups, or documentation that were helpful in solving the challenge.

