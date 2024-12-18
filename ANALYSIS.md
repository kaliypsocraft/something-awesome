# Something Awesome Project 

!!! warning Mission Statement
    This file provides the culmination of research, analysis. The project provides write-ups of picoCTF. The purpose of this is to provide a learning tool for beginners to learn about the foundations of capture-the-flag challenge . PicoCTF is a Jeopardy-style CTF consisting of challenges related to  [cryptography](#cryptography), [web exploitation](#web-exploitation), [forensics](#forensics), [reverse engineering](#reverse-engineering) and [binary exploitation](#binary-exploitation).

## Table of Contents
- [Disclaimer](#disclaimer)
- [Features](#features)
- [Challenges](#challenges)
  - [General Skills](#general-skills)
  - [Cryptography](#cryptography)
  - [Classical Ciphers](#classical-ciphers)
    - [Classical Cipher Notation](#classical-ciphers-notation)
    - [Caesar Cipher](#caesar-cipher)
    - [Caesar Crypt-analysis](#caesar-crypt-analysis)
    - [Vigenere Cipher](#vigenere-cipher)
    - [Vigenere Crypt-analysis](#vigenere-crypt-analysis)
    - [Substitution Cipher](#substitution-cipher)
    - [Substitution Crypt-analysis](#substitution-crypt-analysis)
    - [Classical Cipher Crypt-analysis](#classical-cipher-crypt-analysis)
    - [RSA](#rsa)
    - [RSA Crypt-analysis](#rsa-crypt-analysis)
    - [Side-Channel Attacks](#side-channel-attacks)
  - [Web Exploitation](#web-exploitation)
    - [SQL Injection](#sql-injection)
    - [XSS Injection](#xss-injection)
  - [Forensics](#forensics)
    - [File Formats](#file-formats)
    - [Steganography](#steganography) 
  - [Reverse Engineering](#reverse-engineering)
    - [Disassemblers](#disassemblers)
    - [Debuggers](#debuggers)
  - [Binary Exploitation](#binary-exploitation)
    - [Registers](#registers)
    - [Calling Conventions](#calling-conventions)
    - [Buffer Overflow](#buffer-overflow)
    - [ret2win](#ret2win)
    - [ret2libc](#ret2libc)
    - [GOT](#got)
    - [Format String Vulnerabilities](#format-string-vulnerabilities)

- [Diary](#diary)
  - [Week 1](#week-1)
  - [Week 2](#week-2)
  - [Week 3](#week-3)
  - [Week 4](#week-4)
  - [Week 5](#week-5)
  - [Week 6](#week-6)
  - [Week 7](#week-7)
  - [Week 8](#week-8)
- [Conclusion](#conclusion)
- [References](#references)
## Disclaimer
The information below is to be taken with a grain of salt. It has been my intepretation from the resources I've consumed. There may be some mistakes and details which may be incorrect.

## Problem Sets
!!! info Purpose
    The following sections involve a **theory** component consisting of the basic research and background knowledge required to conduct the CTF. Within each sub-section there is also the practical component which provides a hyperlink to a write-up. The template run-down is given in `SAP_REPORT.md`. It is also on the given Github [link](https://github.com/kaliypsocraft/something-awesome) within `WRITE_UP_TEMPLATE.md`.

## Cryptography
Cryptography is the process of obsfucating information using mathemtical properties. Within CTF challenges they usually begin with basic classical ciphers such as the Caesar cipher. Moderate challenges may include
a substitution cipher or Vigenere ciphers which may require a more sophisticated cryptanalytic attack.

!!! info Classical Ciphers
    These tend to be part of the easy-medium level challenges within the CTF. Classical ciphers in the real world refers to cryptographic schemes which typically were used prior to the 1970s where *strong* algorithms which relied on computers paved the way for modern cryptography. 
    #### Classical Ciphers Notation 
    - $c_i$ is the $i^{th}$ character of the ciphertext.
    - $m_i$ is the $i^{\text{th}}$ character of the decrypted plaintext.
    - $k_i$ is the $i^{\text{th}}$ character of the key.
    - $k$ is the key used during encryption.
    - $||$ means concatentation
### Caesar Cipher
The Caesar Cipher is one of the most simple and recognizable ciphers in the world. It functions by shifting all letters of the alphabet by a fixed number. They are amongst the most **beginner** friendly cryptography challenges.

Suppose we want to encrypt the message $m = m_1 || m_2 || m_3 || ... || m_n$. The encryption algorithm $E$ is defined as:

$$
E(k) = (m_i + k) \mod 26 = c_i
$$

The ciphertext would be:

$$
c = c_1 || c_2 || ... || c_n
$$

Given a ciphertext $c = c_1 || c_2 || c_3 || ... || c_n$, the decryption algorithm $D$ is defined as:

$$
D(k) = (c_i - k) \mod 26 = m_i
$$
![image](https://github.com/user-attachments/assets/7c7de9e7-0ea4-4136-bd1a-496de73eeb3b)
### Caesar Crypt-analysis
Assuming the key-space is consisting of English letters [A-Z], there are only 26 possible keys. Therefore it would be 
trivial for any attacker to brute force all keys. For example,
```py
def decrypt(ciphertext):
    english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    candidate_plaintext = []
    # lower-cases ruins the ASCII calculations
    ciphertext = ciphertext.upper()

    for shift in range(0, 25):
        decrypted_message = ''
        for char in ciphertext:
            if char in alphabet:
                original_index = (alphabet.index(char) - shift) % 26
                decrypted_message += alphabet[original_index]
            else:
                decrypted_message += char 
        candidate_plaintext.append((shift, decrypted_message))
    return results
```
### Vigenere Cipher

The Vigenère cipher is a method of encrypting alphabetic text using a different 'Caesar' key at each index of the key. A keyword is used to determine the shift for each letter in the plaintext. 

Given a plaintext $m = m_1 || m_2 || m_3 || ... || m_n$ and a keyword $k = k_1 || k_2 || k_3 || ... || k_n$, the encryption algorithm $E$ is defined as:

$$c_i = (m_i + k_i) \mod 26$$

Given a ciphertext $c = c_1 || c_2 || c_3 || ... || c_n$ and a repeating key $k = k_1 || k_2 || k_3 || ... || k_n$, the decryption algorithm $D$ is defined as:

$$m_i = (c_i - k_i + 26) \mod 26$$

### Vigenere Crypt-analysis
Unlike a typical Caesar cipher it can be impractical to attempt all $26!$ possible keys. However a frequency analysis attack can be conducted after obtaining the key-size using [Kasiski examination's method](https://en.wikipedia.org/wiki/Kasiski_examination)
### Substitution Cipher
Suppose an example substitution dict is as follows `dict` is as follows 
| Plaintext | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|-----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ciphertext| Q | W | E | R | T | Y | U | I | O | P | A | S | D | F | G | H | J | K | L | Z | X | C | V | B | N | M |

Given a plaintext $m = m_1 || m_2 || m_3 || ... || m_n$ and a substitution dictionary `dict`, the encryption algorithm $E$ is defined as:

$$c_i = dict(m_i)$$

For example, $dict(A) = Q, dict(B) = W \cdots dict(Z) = M$

Given a ciphertext $c = c_1 || c_2 || c_3 || ... || c_n$ and the substitution dictionary `dict`, the decryption algorithm $D$ is defined as:

$$m_i = dict^{-1}(c_i)$$
where, $dict^{-1}$ is as follows (the inverse table)

| Ciphertext | Q | W | E | R | T | Y | U | I | O | P | A | S | D | F | G | H | J | K | L | Z | X | C | V | B | N | M |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Plaintext  | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |

### Substitution Crypt-analysis
Online software usually can easily defeat subsitution ciphers using frequency analysis. 

---

!!! info Modern Cryptography
    These challenges tend to be medium-hard level questions which exploit a deliberate use of *weak* parameters. In the real-world these schemes when used correctly are deemed mathematically strong and secure. Usually they involve the hardness of the discrete logarithm problem or factoring problem. In the case of RSA which most of the intermediate-hardlevel cryptography problems are, it deals with the factoring problem. However, side-channe


### RSA

Perhaps one of the most famous modern-day ciphers, RSA has become a hall of fame candidate in the world of public key cryptography. The security of RSA is derived from the assumed hardness of factoring large integers. 

Given a plaintext message m and a public key $(e, n)$, where $e$ is the encryption exponent and n is the modulus, the encryption algorithm $E$ is defined as:

$$
c = m^e \mod n
$$

Where:
- $c$ is the ciphertext.
- $m$ is the plaintext message.

Given the ciphertext $c$ and a private key $(d, n)$, where $d$ is the decryption exponent, the decryption algorithm $D$ is defined as:

$$
m = c^d \mod n
$$

Where:
- $m$ is the recovered plaintext message.

### Parameter Generation
To generate the keys, the following steps are performed:

1. **Choose two distinct prime numbers** $p$ and $q$.
2. **Compute** $n = p \cdot q.$
3. **Calculate the totient** $φ(n) = (p-1)(q-1).$
4. **Choose an integer** $e$ such that $1 < e < φ(n)$ and $gcd(e, φ(n)) = 1$.
5. **Determine the private exponent** $d$ as the modular multiplicative inverse of $e$ modulo $φ(n)$, satisfying $d ⋅ e ≡ 1 mod φ(n).$


### RSA Crypt-analysis
We must note that the generic RSA, known as textbook RSA is deemed insecure since it is not chosen-plain text secure. An example of a chosen-plaintext attack is conducted in `no padding no problem`.
#### Wiener's Attack
For small private keys $ d $, we can conduct [Wiener's attack](https://en.wikipedia.org/wiki/Wiener%27s_attack), which exploits the fact that if $ d $. A RSA cipher is vulnerable to this if 
1. The modulus $N = pq$ with $q < p < 2q$ 
2. The private exponent $d$ satisfying $d < \frac{1}{3} N^{1/4}$


### Side-Channel Attacks

Modern cryptography when used following correct procedures regarding parameter size and operational security are often infeasible to attack directly. For example it is considered impractical to obtain an AES's 128-bit key using any traditional cryptanalysis. 

However, side-channel attacks can in some cases obtain them using unintended information leaks. An example of a side-channel attack we can conduct in the real world is, consider the following scenario. 

!!! info Analogy
    Suppose you ask your indecisive friend where to eat. You ask them 'Do you want to go to Restaurant A or Restaurant B' They say I don't mind. You say what about Restaurant A, they pause and say ok... But when you say Restaurant B, they immediately say yes. You know it is Restaurant B which they want. This is an pseudo-example :).



Within the cryptography, world side channel attacks come in many forms from timing attacks to power analysis. In the case of `picoCTF` the challenges I conducted focused around a simple abstraction of power analysis. 

### Cryptography Write-Ups
- [La Cifre De](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/la%20cifra%20de/la%20cifra%20de.md)
- [Custom Encryption](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/custom_encryption/custom_encryption.md)
- [Mini RSA](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/mini_rsa/mini_rsa.md)
- [Pixelated](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/pixelated/pixelated.md)
- [Dachshund Attacks](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/dachshund_attacks/dachshund_attacks.md)
- [Mind Your P and Qs](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/mind_your_p_and_qs/mind_your_p_and_qs.md)
- [No Padding No Prob](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/no_padding_no_prob/no_padding_no_prob.md)
- [Substitution 1](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/substitution_1/substitution_1.md)
- [Power Analysis: Warm Up](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/power_analysis_0/power_analysis_0.md)

## Web Exploitation
### SQL Injection
  It is one of the first web exploitation techniques a student learns when undertaking an introduction to security course. It involves an 
  attacker inserting malicious SQL queries into an entry field. It is a common attack vector against websites. It is an example of the dangers of 
  mixing **data** and **control**. 
### XSS Injection
XSS Injections typically involve an attacker injecting malicious HTML into a website. 
Cross-site injections come in three forms - reflected, stored and DOM-based. 


### Web Exploitation Write-Ups
- [Java Code Analysis](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/javacode_analysis/javacode_analysis.md)
- [More SQLi](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/more_sqli/more_sqli.md)
- [Most Cookies](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/most_cookies/most_cookies.md)
- [Picobrowser](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/picobrowser/picobrowser.md)
- [Web Gauntlet 1](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/web_gauntlet_1/web_gauntlet_1.md)
- [Web Gauntlet 2](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/web_gauntlet_2/web_gauntlet_2.md)



!!! info ## Forensics
    Forensics challenges typically involve analysing a static file compared to other challenge-types whereby an executable program/remote server is involved. Within the context of CTFs they require candidates to find or reconstruct hidden information within these static files.
### File Formats/Signatures
Recognising file formats and signatures can be useful in CTF challenges.
File formats are a way for data to be encoded for computer storage. For example, `.pdf` or `.png` files.

 File signatures are used to identify and verify the contents of a file.  It can be found via running `xxd <file_name> | head`. This prints the first 10 lines (given by the `head` command) of a [hexdump](#hexdump) of a file. Running `xxd image-1.png | head` provided the following output: ![alt text](images/image-4.png) 
> Note: first line is PNG

This [page](https://en.wikipedia.org/wiki/List_of_file_signatures) has a table of file signatures. For example this can be useful in challenges where the endianness of a file is swapped. Therefore knowing or revising magic numbers associated with common file types such as `.jpg` can be useful. 

Another useful command is `exiftool <filename>` which also provides the meta-data in the form: ![alt text](images/image-5.png)


### Steganography
Steganography conceals sensitive information within files like images, without obvious signs of hidden data. Unlike encryption, it embeds data discreetly by altering pixels or metadata, making it ideal for secure communication. Usually in CTFs they use LSB Steganography which is insecure as it is so well known.

### Network Analysis
Monitoring and examining network traffic is an essential part of security engineering. It can identify suspicious activity or malware. Tools like Wireshark capture packet data, helping security engineers detect threats, troubleshoot issues, and analyze network performance.
### Forensic Write-Ups
- [Endianess V2](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/endianess_v2/endianess_v2.md)
- [Sleuthkit Apprentice](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/sleuthkit_apprentice/sleuthkit_apprentice.md)
- [Trivial Flag Transfer Protocol](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/trivial_flag_transfer_protocol/trivial_flag_transfer_protocol.md)
- [Eavesdropping](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/eavesdropping/eavesdropping.md)
- [Like 1000](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/like_1000/like_1000.md)
- [Op Orchid](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/op_orchid/op_orchid.md)
- [Sleuthkit Intro](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/sleuthkit_intro/sleuthkit_intro.md)

!!! info ## Reverse Engineering
    TODO: Define Reverse Engineering
    Reverse engineering often requires students to interpret machine code or bytecode to understand its functionality. Once they can interpret the machine code, they typically manipulate it to obtain the flag. In a challenge, a candidate is usually presented with a compiled C program. They must use a combination of disassemblers and debuggers to analyze the program's control flow.
    TODO: Insert typical challenges
### Disassemblers
Disassemblers converts machine code into human readable assembly code - in some cases even into 'pseudo' C such as in BinaryNinja and Ghidra for example. This makes it an excellent tool for reverse engineering challenges as it enables the candidate to have an enhanced understanding of the control flow. Disassemblers such as BinaryNinja also provide a control-flow graph view to provide a clearer picture of the logic-flow of code.

![alt text](images/image-3.png)
> BinaryNinja's graph view - Credits: https://binary.ninja/

### Debuggers
Debuggers are used for dynamic code analysis enabling a user to view and alter the state of a program in run-time. `gdb` (GNU debugger) is a common debugger used in CTFs in general, for example above in [binary exploitation](#binary-exploitation).
### Reverse Engineering Write-Ups
- [Crack Me 0x100](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/crack_me_0x100/crack_me_0x100.md)
- [Picker 1](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/picker_1/picker_1.md)
- [Picker 2](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/picker_2/picker_2.md)
- [Picker 3](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/picker_3/picker_3.md)
- [Packer](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/packer/packer.md)
- [Win Anti Dbg 0x100](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/win_anti_dbg_0x100/win_anti_dbg_0x100.md)
- [GDB Baby Step 4](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/gdb_baby_step_4/gdb_baby_step_4.md)
- [Keygenme](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/keygenme/keygenme.md)
- [Not Crypto](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/not_crypto/not_crypto.md)


## Binary Exploitation


![alt text](images/image-2.png)
> Image courtesy of [here](https://www.cameronwickes.co.uk/stack-frames-pointers/)

### Registers
Registers are accessible memory locations within a processor that hold data crucial for computation, such as memory addresses, instructions, and numbers used for calculations. In CTFs, understanding various registers is essential for tracking the **return address**, **stack pointer**, and **base pointers**.

Modern processors typically have either 32-bit or 64-bit registers, meaning they can hold up to 32 or 64 bits of data, respectively. Key registers for binary exploitation include:
- **Instruction Pointer**: Holds the address of the next instruction to be executed.
  - `eip` (32-bit)
  - `rip` (64-bit)
- **Stack Pointer**: Points to the top of the stack.
  - `esp` (32-bit)
  - `rsp` (64-bit)

![Example of 32-bit registers denoted by `e`](images/image-1.png)
> Example of 32-bit registers

![Example of 64-bit registers denoted by `r`](images/image.png)
> Example of 64-bit registers

---

### Calling Conventions
Calling conventions are standardized ways of passing function parameters, either on the stack or stored in registers. This standardization enables interoperability between machines and compilers. If `Machine A` and `Machine B` used different conventions for passing arguments, they could produce different outputs for the same function.

In a 32-bit system, function arguments are typically pushed onto the stack **from right to left**. For example:

```c
int equation(int a, int b, int c) {
  return a + b - c;
}

```
The order of arguments pushed onto the stack would be: c $\rightarrow$ b $\rightarrow$ a. If this convention is not followed, the function may behave unexpectedly:

```
equation(1, 2, 3) = 0
equation(3, 2, 1) = 4

```
For 64-bit systems it is different so be careful when conducting the exercises.



### Global Offset Table (GOT) / Procedure Linkage Table (PLT)

The Global Offset Table (GOT) and Procedure Linkage Table (PLT) are tables used in dynamically linked executables to resolve function addresses at runtime. Dynamically linked executables can be identified by running `file <filename>`. These executables rely on functions that are not directly compiled into the binary but instead reference external shared libraries.

**Analogy**

Consider the PLT as a new retail shop worker, while the GOT is a device the worker uses to record where particular items are located. Imagine a binary as a customer who asks the worker where to find printf. Since the worker (PLT) is new, they don't know immediately and must get help from a friend called the Dynamic Linker. Together, they locate printf and record its address in the GOT. Now, each time the customer asks for printf, the PLT can simply direct the customer to the stored address in the GOT.

In binary exploitation, an attacker can modify the GOT to redirect function calls, which is useful in certain types of attacks like ret2libc. In this analogy, let's assume that the GOT device can be easily manipulated by an attacker named Eve. Eve could change the address stored in the GOT to point to malicious code or use the stored information to execute harmful actions.


### ret2libc
ret2libc attacks aim to execute code in the C standard library (libc) to gain shell access or execute other functions on a remote server. To achieve this, the attacker:

Leverages the GOT to obtain the base address of libc.
Locates the addresses of system, a command string like /bin/sh, and exit. I like to call system and /bin/sh (Bonnie and Clyde) as they typically are the main culprits in my attacks.
Constructs input that sets the return address to system, with /bin/sh as the argument.
This approach allows attackers to bypass the need for shellcode by leveraging existing code in the binary.

Note: There are differences between 32-bit and 64-bit architectures.

### Format String Vulnerabilities
A format string vulnerability occurs when user input is improperly passed as the format argument to variadic functions (which can take a variable number of parameters), such as printf or scanf. For example, if the program accepts unchecked input from the user, an attacker might inject a format string like %x to read memory or %n to write to specific addresses. This vulnerability can lead to memory leakage or even allow code execution if exploited correctly.

```c
char str[] = "Hello world!"
printf("%s", &str)
```
> The `printf` function expects a single argument.

A vulnerable example is, 

```c
printf("%p %p %p %p %p %p")
```
> The `printf` function expects 5 arguments but receives none from the user. It then reads data from the stack which it may unauthorised to do so.

![alt text](images/image-14.png)

> Photo credits: [here](https://www.youtube.com/watch?v=QOgD3jPHyRY)

For example, if the format string is "`%x.%x.%x.%x`", printf will output four consecutive values from the stack in hexadecimal, potentially exposing critical data such as memory addresses, return pointers, or hidden values. i.e. conduct arbitary reads

Additionally, format strings like "`%n$x`" allow an attacker to specify which stack argument to read, providing more control over what is accessed.

One of the most dangerous format specifiers is `%n`, which causes `printf` to write the number of characters printed so far into a memory address specified by the attacker. This can be exploited to overwrite sensitive areas in memory - i.e. conduct arbitary writes.

For example, suppose we want to override a variable on the stack. We can write to this address with a new value we want.

Example payload 1:
Given an offset of 1, we write 5 $\rightarrow$ 0x0804a048 and 10 $\rightarrow$ 0x0804a04c
>`%5c%6$lln%5c%7$hhnaaH\xa0\x04\x08L\xa0\x04\x08`

Example payload 2:
Given an offset of 1, we write 0 $\rightarrow$ 0x0804a048 and 5 $\rightarrow$ 0x0804a04c
>`%5$lln%5c%6$hhnaH\xa0\x04\x08L\xa0\x04\x08`

NOTE: `L` $\rightarrow$ `\x4c` and `H` $\rightarrow$ `\x48`

### Binary Exploitation Write-Ups
- [Basic File Exploit](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/basic_file_exploit/basic_file_exploit.md)
- [Buffer Overflow 2](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/buffer_overflow_2/buffer_overflow_2.md)
- [Fmt Str 2](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/fmt_str_2/fmt_str_2.md)
- [Heap 1](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/heap_1/heap_1.md)
- [Heap 2](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/heap_2/heap_2.md)
- [Heap 3](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/heap_3/heap_3.md)
- [VNE](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/vne/vne.md)
- [Here is Libc](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/here_is_libc/here_is_libc.md)
- [Ropfu](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/ropfu/ropfu.md)
---

!!! info Conclusion
    The information provided in this document is only a subset of the vast world that is the cyber-security community. The information provided is all the research conducted during the solving of `picoCTF` challenges. Please excuse some of the information as I was just a beginner through this whole process. It is an iterative process to becoming a competent security engineer.

## References

- Security Stack Exchange. (2016). Why must a ret2libc attack follow the order system; exit; command? Available at: https://security.stackexchange.com/questions/136647/why-must-a-ret2libc-attack-follow-the-order-system-exit-command/136659#136659 (Accessed: 3 November 2024).

- Long Le. (2016). PEDA - Python Exploit Development Assistance for GDB. Available at: https://github.com/longld/peda (Accessed: 3 November 2024).

- HackTricks. (2024). ROP (Return-Oriented Programming) - Binary Exploitation. Available at: https://book.hacktricks.xyz/binary-exploitation/rop-return-oriented-programing (Accessed: 3 November 2024).

- CS6265 Course, Georgia Tech. (2024). Advanced ROP Tutorial. Available at: https://tc.gts3.org/cs6265/tut/tut06-02-advrop.html (Accessed: 3 November 2024).

- Chester Rebeiro, Indian Institute of Technology Madras. (2024). Buffer Overflows. Available at: https://www.cse.iitm.ac.in/~chester/courses/17o_sse/slides/3_BufOverflows.pdf (Accessed: 3 November 2024).

- Total Phase, Inc. (2023). What is a Register in a CPU and How Does It Work? Available at: https://www.totalphase.com/blog/2023/05/what-is-register-in-cpu-how-does-it-work/ (Accessed: 3 November 2024).

- Automox (n.d.). Vulnerability Definition: Use After Free. Available at: [https://www.automox.com/blog/vulnerability-definition-use-after-free](https://www.automox.com/blog/vulnerability-definition-use-after-free) (Accessed: 3 November 2024).
- CWE (n.d.). Use After Free. Available at: [https://cwe.mitre.org/data/definitions/416.html](https://cwe.mitre.org/data/definitions/416.html) (Accessed: 3 November 2024).
- CTF Recipes (n.d.). Heap Exploitation: Use After Free. Available at: [https://www.ctfrecipes.com/pwn/heap-exploitation/use-after-free](https://www.ctfrecipes.com/pwn/heap-exploitation/use-after-free) (Accessed: 3 November 2024).
- The Hacker News (2024). Mozilla Warns of Active Exploitation. Available at: [https://thehackernews.com/2024/10/mozilla-warns-of-active-exploitation-in.html](https://thehackernews.com/2024/10/mozilla-warns-of-active-exploitation-in.html) (Accessed: 3 November 2024).
- NIST (2023). FIPS 197 - Advanced Encryption Standard (AES). Available at: [https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf) (Accessed: 3 November 2024).
- Stanford University (n.d.). A Survey of RSA Cryptography. Available at: [https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf) (Accessed: 3 November 2024).
- Varonis (n.d.). How to Use Ghidra. Available at: [https://www.varonis.com/blog/how-to-use-ghidra](https://www.varonis.com/blog/how-to-use-ghidra) (Accessed: 3 November 2024).
- Real Python (n.d.). Python eval Function. Available at: [https://realpython.com/python-eval-function/](https://realpython.com/python-eval-function/) (Accessed: 3 November 2024).
- Binary Ninja (n.d.). Available at: [https://binary.ninja/](https://binary.ninja/) (Accessed: 3 November 2024).
- Autopsy (n.d.). Digital Forensics. Available at: [https://www.autopsy.com/](https://www.autopsy.com/) (Accessed: 3 November 2024).
- Coastal White (n.d.). Modeling AES with Power Analysis. Available at: [https://coastalwhite.github.io/intro-power-analysis/aes/modeling.html](https://coastalwhite.github.io/intro-power-analysis/aes/modeling.html) (Accessed: 3 November 2024).
- The Sleuth Kit (n.d.). Available at: [https://www.sleuthkit.org/sleuthkit/docs.php](https://www.sleuthkit.org/sleuthkit/docs.php) (Accessed: 3 November 2024).
- Cryptii (n.d.). Vigenère Cipher. Available at: [https://cryptii.com/pipes/vigenere-cipher](https://cryptii.com/pipes/vigenere-cipher) (Accessed: 3 November 2024).
- GitHub (n.d.). PayloadsAllTheThings: SQL Injection - SQLite Injection. Available at: [https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md) (Accessed: 3 November 2024).
- CTF 101 (n.d.). Web Exploitation Overview. Available at: [https://ctf101.org/web-exploitation/overview/](https://ctf101.org/web-exploitation/overview/) (Accessed: 3 November 2024).
- W3Schools (n.d.). SQL Injection. Available at: [https://www.w3schools.com/sql/sql_injection.asp](https://www.w3schools.com/sql/sql_injection.asp) (Accessed: 3 November 2024).
- OWASP (n.d.). Cross-Site Scripting (XSS). Available at: [https://owasp.org/www-community/attacks/xss/](https://owasp.org/www-community/attacks/xss/) (Accessed: 3 November 2024).


#### Other 
- [Recent example of Firefox case study](#https://thehackernews.com/2024/10/mozilla-warns-of-active-exploitation-in.html)
- [How the best hackers learn their craft](https://www.youtube.com/watch?v=6vj96QetfTg)
- [How processor clocks work](https://www.youtube.com/watch?v=PVNAPWUxZ0g)

