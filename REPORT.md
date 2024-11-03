# Something Awesome Project 

!!! warning Mission Statement
    This file provides the culmination of research, analysis 
    The project provides write-ups of picoCTF. The purpose of this is to provide a learning tool for
    beginners to learn about the foundations of capture-the-flag challenges. PicoCTF is a Jeopardy-style
    CTF consisting of challenges related to  [cryptography](#cryptography), [web exploitation](#web-exploitation), [forensics](#forensics), [reverse engineering](#reverse-engineering) and [binary exploitation](#binary-exploitation).

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
    - [PHP](#php)
    
  - [Forensics](#forensics)
    - [File Formats](#file-formats)
    - [Meta-Data](#meta-data)
    - [Disk Imaging](#disk-imaging)
    - [Steganography](#steganography)
    
  - [Reverse Engineering](#reverse-engineering)
    - [Disassemblers](#disassemblers)
    - [Debuggers](#debuggers)
    
  - [Binary Exploitation](#binary-exploitation)
    - [Stack](#stack)
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
Cryptography is the process of obsfucating information from unauthorised people. Usually modern cryptographic algorithms must
satisfy three properties: 
TODO: Add definitions
1. Confidentiality
2. Integrity
3. Authentication

Within CTF challenges they usually begin with basic classical ciphers such as the Caesar cipher. Moderate challenges may include
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
The Caesar Cipher is one of the most simple and recognizable ciphers in the world named after the Roman leader Julius Caesar. It functions by shifting all letters of the alphabet by a fixed number. They are amongst the most **beginner** friendly cryptography challenges.

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
```
def decrypt(ciphertext):
    english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    candidate_plaintext = []
    ciphertext = ciphertext.upper()

    # Loops through all possible shifts 
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

The Vigenère cipher is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution. A keyword is used to determine the shift for each letter in the plaintext. It essentially encrypts each letter of the plain-text

Given a plaintext $m = m_1 || m_2 || m_3 || ... || m_n$ and a keyword $k = k_1 || k_2 || k_3 || ... || k_n$, the encryption algorithm $E$ is defined as:

$$c_i = (m_i + k_i) \mod 26$$

Given a ciphertext $c = c_1 || c_2 || c_3 || ... || c_n$ and a repeating key $k = k_1 || k_2 || k_3 || ... || k_n$, the decryption algorithm $D$ is defined as:

$$m_i = (c_i - k_i + 26) \mod 26$$

### Vigenere Crypt-analysis
Unlike a typical Caesar cipher it can be impractical to attempt all $26!$ possible keys. However a frequency analysis attack can be conducted after obtaining the key-size. 
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

!!! info Modern Cryptography
    These challenges tend to be medium-hard level questions which exploit a deliberate use of *weak* parameters. In the real-world these schemes when used correctly are deemed mathematically strong and secure. However, side-channe

### RSA

Perhaps one of the most famous modern-day ciphers, RSA has become a hall of fame candidate in the world of public key cryptography. The security of RSA is derived from the assumed hardness of factoring large integers.  

### RSA Crypt-analysis
For small private keys $d$, we can conduct Wieners attack

For small modulus $n$, one can easily bruteforce the factoring with `gmpy`.

For small exponent $e$ and 

### Side-Channel Attacks

Modern cryptography when used following correct procedures regarding parameter size and operational security are often infeasible to attack directly. For example it is considered impractical to obtain an AES's 128-bit key using any traditional cryptanalysis. 

However, side-channel attacks can in some cases obtain them using unintended information leaks. An example of a side-channel attack we can conduct in the real world is, consider the following scenario. 
> Suppose you suspect your friend of taking your popsticle.

Within the cryptography world side channel attacks come in many forms from timing attacks to power analysis. In the case of `picoCTF` the challenges I conducted focused around power analysis. 

### Cryptography Write-Ups
- [Lac Cifre De](ttps://github.com/kaliypsocraft/something-awesome/blob/main/crypto/custom_encryption/custom_encryption.md)
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

### PHP
TODO: Add content for PHP.

### Web Exploitation Write-Ups
- [Java Code Analysis](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/javacode_analysis/javacode_analysis.md)
- [More SQLi](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/more_sqli/more_sqli.md)
- [Most Cookies](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/most_cookies/most_cookies.md)
- [Picobrowser](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/picobrowser/picobrowser.md)
- [Web Cookies](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/web_cookies/web_cookies.md)
- [Web Gauntlet 1](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/web_gauntlet_1/web_gauntlet_1.md)
- [Web Gauntlet 2](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/web_gauntlet_2/web_gauntlet_2.md)
- [Notepad](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/notepad/notepad.md)
- [Javascript Kiddie](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/javascript_kiddie/javascript_kiddie.md)


!!! info ## Forensics
    Forensics challenges typically involve analysing a static file compared to other challenge-types whereby an executable program/remote server is involved. Within the context of CTFs they require candidates to find or reconstruct hidden information within these static files.
### File Formats/Signatures
Recognising file formats and signatures can be useful in CTF challenges.
File formats are a way for data to be encoded for computer storage. For example, `.pdf` or `.png` files.

 File signatures are used to identify and verify the contents of a file.  It can be found via running `xxd <file_name> | head`. This prints the first 10 lines (given by the `head` command) of a [hexdump](#hexdump) of a file. Running `xxd image-1.png | head` provided the following output: ![alt text](images/image-4.png) 
> Note: first line is PNG

This [page](https://en.wikipedia.org/wiki/List_of_file_signatures) has a table of file signatures. For example this can be useful in challenges where the endianness of a file is swapped. Therefore knowing or revising magic numbers associated with common file types such as `.jpg` can be useful. 

Another useful command is `exiftool <filename>` which also provides the meta-data in the form: ![alt text](images/image-5.png)

### Disk Imaging
Disk images serve as a snapshot of 

### Steganography
Steganography is the act of hiding/obsfucating sensitive data within an image.
### Network Analysis
Analysing network traffic is an essential aspect of security engineering. 
### Forensic Write-Ups
- [Disk Disk Sleuth](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/disk_disk_sleuth/disk_disk_sleuth.md)
- [Endianess V2](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/endianess_v2/endianess_v2.md)
- [Op Oni](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/op_oni/op_oni.md)
- [Sleuthkit Apprentice](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/sleuthkit_apprentice/sleuthkit_apprentice.md)
- [Trivial Flag Transfer Protocol](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/trivial_flag_transfer_protocol/trivial_flag_transfer_protocol.md)
- [Eavesdropping](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/eavesdropping/eavesdropping.md)
- [Like 1000](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/like_1000/like_1000.md)
- [Op Orchid](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/op_orchid/op_orchid.md)
- [Sleuthkit Intro](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/sleuthkit_intro/sleuthkit_intro.md)
- [Web Net 0](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/web_net_0/web_net_0.md)

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
TODO: Add format strings and buffer overflow definition
### Stack
The stack exists in a computer's RAM and 


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

### Buffer Overflow
A buffer overflow occurs when data exceeds the allocated memory buffer size, potentially accessing or overwriting other areas of memory. Unsafe functions like gets can lead to buffer overflows. For example:
``` c

void unsafe() {
  int buffer[5];
  gets(buffer);
}
```

In this case, if a user inputs more than 5 bytes of data, they can access unintended areas of the stack.

### Global Offset Table (GOT) and Procedure Linkage Table (PLT)
The Global Offset Table (GOT) and Procedure Linkage Table (PLT) are tables used in dynamically linked executables to resolve function addresses at runtime. When a function is first called, its address is stored in the GOT via the PLT, so future calls can directly access the function without additional lookups.

- PLT: Acts as an intermediary, initially directing calls to dynamically linked functions to their proper locations by using the GOT.
- GOT: Stores the resolved addresses of functions, allowing direct access on subsequent calls.
In binary exploitation, modifying the GOT can enable redirection of function calls, which is helpful in specific types of attacks like ret2libc.

### ret2win
In ret2win challenges, the goal is to override the return address (stored in eip on a 32-bit system or rip on a 64-bit system) with the address of a function that prints or contains the flag. These challenges typically involve:

Finding the address of the target function.
Using input to overflow the stack and overwrite the return address, redirecting it to the target function.

### ret2libc
ret2libc attacks aim to execute code in the C standard library (libc) to gain shell access or execute other functions on a remote server. To achieve this, the attacker:

Leverages the GOT to obtain the libc base address.
Locates the addresses of system, a command string like /bin/sh, and exit.
Constructs an input that sets the return address to system, with /bin/sh as the argument.
This approach allows attackers to bypass the need for shellcode by leveraging already-present code in the binary.

Note there are differences between 32-bit and 64-bit architectures.
### Format String Vulnerabilities
A format string vulnerability occurs when user input is improperly passed as the format argument to variadic functions (can take a variable number of parameters) like `printf` or `scanf`. For example, 

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
Given an offset of 1, we write 0 $\rightarrow$ 0x0804a048 and 0 $\rightarrow$ 0x0804a04c
> `%3$llnaaH\xa0\x04\x08`

Example payload 2:
Given an offset of 1, we write 5 $\rightarrow$ 0x0804a048 and 10 $\rightarrow$ 0x0804a04c
>`%5c%6$lln%5c%7$hhnaaH\xa0\x04\x08L\xa0\x04\x08`

Example payload 3:
Given an offset of 1, we write 5 $\rightarrow$ 0x0804a048 and 0 $\rightarrow$ 0x0804a04c
>`%5c%4$llnaaaH\xa0\x04\x0`

Example payload 4:
Given an offset of 1, we write 0 $\rightarrow$ 0x0804a048 and 5 $\rightarrow$ 0x0804a04c
>`%5$lln%5c%6$hhnaH\xa0\x04\x08L\xa0\x04\x08`

NOTE: `L` $\rightarrow$ `\x4c` and `H` $\rightarrow$ `\x48`

TODO: Insert more information about broader topics
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

## Conclusion

## References