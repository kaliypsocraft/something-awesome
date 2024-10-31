# CTF Write-Up: [Challenge Name][Challenge Type]

## Description
>A brief description of the challenge, including its title, type (e.g., web, crypto, pwn)


## Flag
The flag you obtained after solving the challenge. (e.g., `picoCTF{example_flag}`)

## Difficulty
- **Difficulty Level:** [easy/medium/hard]

## Tools Used
- List any tools or resources you used to solve the challenge (e.g., Wireshark, Burp Suite, Python, etc.).

## Write-Up

### Preparatory Phase
- Describe the first step you took to approach the challenge. Include any commands, scripts, or techniques used.

### Attack Phase
Upon connecting to the host and port, we are greeted with values $e$, $n$, and $c$. I ran the connection multiple times to check if the exponents and variables changed, and they did.

Using the clue that $d$ is small suggests attempting [[Wiener's attack]]. To execute this, download `import owiener` and run `d = owiener.attack(e, n)`. 

Next, obtain $m$ using the equation $c^{d} \mod n$. I attempted to decode the result as ASCII, which initially yielded some garbled output. However, a simple `long_to_bytes()` function successfully converted the result into a readable format.
### Final Solution/Payload


### Lessons Learnt

## References
- Link to any external resources, write-ups, or documentation that were helpful in solving the challenge.

