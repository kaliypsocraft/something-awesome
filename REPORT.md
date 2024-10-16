# Something Awesome Project 

The project provides write-ups of picoCTF. The purpose of this is to provide a learning tool for
beginners to learn about the foundations of capture-the-flag challenges. PicoCTF is a Jeopardy-style
CTF consisting of challenges related to [general skills](#general-skills), [cryptography](#cryptography), [web exploitation](#web-exploitation), [forensics](#forensics), [reverse engineering](#reverse-engineering) and [binary exploitation](#binary-exploitation).
## Table of Contents
- [Features](#features)
- [Challenges](#challenges)
  - [General Skills](#general-skills)
  - [Cryptography](#cryptography)
    - [Caesar Cipher](#caesar-cipher)
    - [Vigenere Cipher](#vigenere-cipher)
    - [Substitution Cipher](#substitution-cipher)
    - [Classical Cipher Crypt-analysis](#classical-cipher-crypt-analysis)
    - [RSA](#rsa)
    - [RSA Crypt-analysis](#rsa-crypt-analysis)
    - [Diffie Hellman](#diffie-hellman)
    - [Diffie Hellman Crypt-analysis](#diffie-hellman-crypt-analysis)
    - [Side-Channel Attacks](#side-channel-attacks)
    - [Post Quantum Cryptography](#post-quantum-cryptography)
  
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
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
## Features
TODO: Add instructions on the basic flow of the report
## Challenges
List the key features of your project.
## General Skills
General skills consist of using the basic tools and tricks of the trade such as Linux commands e.t.c. The skills learnt from these
challenges form the prequesite knowledge required for not just CTFs but computing literacy for a computer-science student. 
## Cryptography
Cryptography is the process of obsfucating information from unauthorised people. Usually modern cryptographic algorithms must
satisfy three properties: 
TODO: Add definitions
1. Confidentiality
2. Integrity
3. Authentication

Within CTF challenges they usually begin with basic classical ciphers such as the Caesar cipher. Moderate challenges may include
a substitution cipher or Vigenere ciphers which may require a more sophisticated cryptanalytic attack.
### Caesar Cipher
TODO: Add content for Caesar Cipher.

### Vigenere Cipher
TODO: Add content for Vigenere Cipher.

### Substitution Cipher
TODO: Add content for Substitution Cipher.

### Classical Cipher Crypt-analysis
TODO: Add content for Classical Cipher Crypt-analysis.

### RSA
TODO: Add content for RSA.

### RSA Crypt-analysis
TODO: Add content for RSA Crypt-analysis.

### Diffie Hellman
TODO: Add content for Diffie Hellman.

### Diffie Hellman Crypt-analysis
TODO: Add content for Diffie Hellman Crypt-analysis.

### Side-Channel Attacks
TODO: Add content for Side-Channel Attacks.

### Post Quantum Cryptography
TODO: Add content for Post Quantum Cryptography.
TODO: Insert typical challenges

TODO: Insert more information about broader topics
#### Medium
- [Custom Encryption](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/custom_encryption/la_cifra_de.md)
- [Mini RSA](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/mini_rsa/mini_rsa.md)
- [Pixelated](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/pixelated/pixelated.md)
- [RSA Oracle](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/rsa_oracle/rsa_oracle.md)
- [Dachshund Attacks](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/dachshund_attacks/dachshund_attacks.md)
- [Mind Your P and Qs](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/mind_your_p_and_qs/mind_your_p_and_qs.md)
- [No Padding No Prob](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/no_padding_no_prob/no_padding_no_prob.md)
- [Spelling Quiz](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/spelling_quiz/spelling_quiz.md)
- [Substitution 1](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/substitution_1/substitution_1.md)
- [Substitution 2](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/substitution_2/substitution_2.md)

#### Hard
- [SRA](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/sra_hard/sra_hard.md)
- [Power Analysis: Warm Up](https://github.com/kaliypsocraft/something-awesome/blob/main/crypto/power_analysis_0/power_analysis_0.md)

## Web Exploitation
### SQL Injection
  It is one of the first web exploitation techniques a student learns when undertaking an introduction to security course. It involves an 
  attacker inserting malicious SQL queries into an entry field. It is a common attack vector against websites. It is an example of the dangers of 
  mixing **data** and **control**. 
### XSS Injection
TODO: Add content for XSS Injection.

### PHP
TODO: Add content for PHP.
TODO: Add other web exploitation attack vectors

TODO: Insert typical challenges

TODO: Insert more information about broader topics
### picoCTF Challenges
#### Medium
- [Java Code Analysis](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/javacode_analysis/javacode_analysis.md)
- [More SQLi](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/more_sqli/more_sqli.md)
- [Most Cookies](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/most_cookies/most_cookies.md)
- [Picobrowser](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/picobrowser/picobrowser.md)
- [SQL Direct](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/sql_direct/sql_direct.md)
- [Web Cookies](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/web_cookies/web_cookies.md)
- [Web Gauntlet 1](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/web_gauntlet_1/web_gauntlet_1.md)
- [Web Gauntlet 2](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/web_gauntlet_2/web_gauntlet_2.md)

#### Hard
- [Notepad](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/notepad/notepad.md)
- [Javascript Kiddie](https://github.com/kaliypsocraft/something-awesome/blob/main/web_exploit/javascript_kiddie/javascript_kiddie.md)

## Forensics
### File Formats
TODO: Add content for File Formats.

### Meta-Data
TODO: Add content for Meta-Data.

### Disk Imaging
TODO: Add content for Disk Imaging.

### Steganography
TODO: Add content for Steganography.
#### Medium
- [Disk Disk Sleuth](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/disk_disk_sleuth/disk_disk_sleuth.md)
- [Endianess V2](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/endianess_v2/endianess_v2.md)
- [Op Oni](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/op_oni/op_oni.md)
- [Packets Primer](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/packets_primer/packets_primer.md)
- [Sleuthkit Apprentice](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/sleuthkit_apprentice/sleuthkit_apprentice.md)
- [Trivial Flag Transfer Protocol](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/trivial_flag_transfer_protocol/trivial_flag_transfer_protocol.md)
- [Eavesdropping](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/eavesdropping/eavesdropping.md)
- [Like 1000](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/like_1000/like_1000.md)
- [Op Orchid](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/op_orchid/op_orchid.md)
- [Scan Surprise](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/scan_surprise/scan_surprise.md)
- [Sleuthkit Intro](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/sleuthkit_intro/sleuthkit_intro.md)

#### Hard
- [Web Net 0](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/web_net_0/web_net_0.md)
- [Investigative Reversing 1](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/investigative_reversing_1/investigative_reversing_1.md)
- [Investigative Reversing 2](https://github.com/kaliypsocraft/something-awesome/blob/main/forensics/investigative_reversing_2/investigative_reversing_2.md)


## Reverse Engineering
TODO: Define Reverse Engineering
Reverse engineering often requires students to interpret machine code or bytecode to understand its functionality. Once they can interpret the machine code, they typically manipulate it to obtain the flag. In a challenge, a candidate is usually presented with a compiled C program. They must use a combination of disassemblers and debuggers to analyze the program's control flow.
TODO: Insert typical challenges
### Disassemblers
TODO: Add content for Disassemblers.

### Debuggers
TODO: Add content for Debuggers.
TODO: Insert more information about broader topics
#### Medium
- [Crack Me 0x100](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/crack_me_0x100/crack_me_0x100.md)
- [Picker 1](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/picker_1/picker_1.md)
- [Picker 2](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/picker_2/picker_2.md)
- [Picker 3](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/picker_3/picker_3.md)
- [Win Anti Dbg 0x200](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/win_anti_dbg_0x200/win_anti_dbg_0x200.md)
- [GDB Baby Step 4](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/gdb_baby_step_4/gdb_baby_step_4.md)
- [Packer](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/packer/packer.md)
- [Win Anti Dbg 0x100](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/win_anti_dbg_0x100/win_anti_dbg_0x100.md)
- [Win Anti Dbg 0x300](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/win_anti_dbg_0x300/win_anti_dbg_0x300.md)

#### Hard
- [Keygenme](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/keygenme/keygenme.md)
- [OTP Implementation](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/otp_implementation/otp_implementation.md)
- [Not Crypto](https://github.com/kaliypsocraft/something-awesome/blob/main/reverse_eng/not_crypto/not_crypto.md)


## Binary Exploitation
TODO: Add format strings and buffer overflow definition
### Stack
TODO: Add content for Stack.

### Registers
TODO: Add content for Registers.

### Calling Conventions
TODO: Add content for Calling Conventions.

### Buffer Overflow
TODO: Add content for Buffer Overflow.

### ret2win
TODO: Add content for ret2win.

### ret2libc
TODO: Add content for ret2libc.

### GOT
TODO: Add content for GOT.

### Format String Vulnerabilities
TODO: Add content for Format String Vulnerabilities.
TODO: Insert typical challenges

TODO: Insert more information about broader topics
#### Medium
- [Basic File Exploit](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/basic_file_exploit/basic_file_exploit.md)
- [Buffer Overflow 2](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/buffer_overflow_2/buffer_overflow_2.md)
- [Clutter Overflow](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/clutter_overflow/clutter_overflow.md)
- [Fmt Str 2](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/fmt_str_2/fmt_str_2.md)
- [Fmt Str 3](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/fmt_str_3/fmt_str_3.md)
- [Heap 1](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/heap_1/heap_1.md)
- [Heap 2](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/heap_2/heap_2.md)
- [Heap 3](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/heap_3/heap_3.md)
- [VNE](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/vne/vne.md)
- [Two Sum](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/two_sum/two_sum.md)
#### Hard
- [Buffer Overflow 3](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/buffer_overflow_3/buffer_overflow_3.md)
- [Function Overwrite](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/function_overwrite/function_overwrite.md)
- [Ropfu](https://github.com/kaliypsocraft/something-awesome/blob/main/bin_exploit/ropfu/ropfu.md)
## Diary
  The diary serves as a logbook for weekly evaluations in order to enhance productivity and to maintain purpose. 
  Each week consists of a more detailed overview of what is conducted in order to advance the state of the project. 
  The intention behind the diary is to be mindful and to maximise intent with all activities on a day to day basis.
## Week 1
### What I did?
- Week 1 was just getting the cogs moving and selecting between projects. At this stage, I was debating between a cryptography research project or a CTF write-up.

### What I need to improve?
- Reduce screen time
- Be swift and decisive with choosing a project

### How to fix errors?
- Be mindful and deliberate with the selection of tasks and projects.

## Week 2
### What I did?
- Solving SQL Injections and Buffer Overflows (being hands-on)
- These tasks further assisted me on my CTF write-ups/tutorial project.
- They exposed me to more CTF-related challenges and gave me some insight into the thinking patterns required for CTFs and the psychology behind them.

### What I need to improve?
- Develop a deeper understanding of SQL injection techniques and their real-world applications.
- Practice more buffer overflow exercises to improve my confidence in exploiting this vulnerability.

### How to fix errors?
- Use online platforms like Hack The Box and TryHackMe to practice SQL injections and buffer overflow challenges.
- Set weekly goals for specific vulnerabilities to focus on, ensuring steady progress.

## Week 3
### What I did?
- Conducted Wargames specifically on XSS Injection-related tasks.
- Continued my Something Awesome Project - made a website via Canva.
- Wrote Something Awesome Project Write-Ups on a markdown file ready to transfer over.
- Finished 12 CTF challenges related to SAP.
- Attended B-Sides!
- There was a talk on exploitation of AI models and modern cryptographic attacks which intrigued me.
- Engaged in discussions with industry professionals during the B-Sides event, gaining insights into emerging trends in cybersecurity.
- Developed a better understanding of different types of XSS attacks and their mitigations.

### What I need to improve?
- Strengthen my knowledge of different types of web vulnerabilities beyond XSS.
- Enhance my ability to articulate findings and strategies in my write-ups for better clarity.

### How to fix errors?
- Dedicate time to researching and practicing additional web vulnerabilities, such as CSRF and RCE.
- Seek feedback on my write-ups from peers or mentors to improve my communication skills and technical accuracy.

## Week 4
### What I did?
- Completed advanced web exploitation challenges, particularly focusing on session management vulnerabilities.
- Began learning about heap exploitation techniques, which will add depth to my Something Awesome Project.
- Drafted additional CTF write-ups for the ongoing project, covering techniques like Cross-Site Scripting (XSS) and SQL Injection.

### What I need to improve?
- Refine my understanding of heap exploitation, as some concepts are still unclear.
- Improve time management between different tasks (CTF challenges, research, and project write-ups).

### How to fix errors?
- Set aside focused study sessions specifically for heap exploitation concepts, using resources like wargames or tutorials.
- Create a more structured daily schedule to balance CTF challenges, project progress, and personal research.

## Week 5
  ### What I did?
- This week conducted format strings practice on picoCTF as that is what we learnt in the Thursday Extended lecture
- Conducted post-quantum cryptography research specifically post-quantum digital signatures
- Read into a data structure 
  ### What I need to improve?
- Once again phone has stolen my attention at times.
- Rushing into a problem rather than taking the time to slow down and think.
- Hitting dead ends in problems and feeling demoralised.
  ### How to fix errors?
- Set aside time to be cognizant of *how to* solve a problem rather than diving straight in.
- Be mindful and intentional in everything I do and be methodical in my thinking
## Week 6


## Week 7


## Week 8

### Building

Explain how to build the project. Include any specific commands or build systems used.

```bash
# Example build command
make
