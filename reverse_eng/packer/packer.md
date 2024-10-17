# CTF Write-Up: [Challenge Name]

## Description
A brief description of the challenge, including its title, type (e.g., web, crypto, pwn)

## Flag
The flag you obtained after solving the challenge. (e.g., `picoCTF{example_flag}`)

## Difficulty
- **Difficulty Level:** [easy/medium/hard]

## Tools Used
- List any tools or resources you used to solve the challenge (e.g., Wireshark, Burp Suite, Python, etc.).

## Write-Up

### Step 1: [Prepartory]
- I first ran `gdb ./out` and received no information. This suggested all the symbols were somehow removed and not present:
![alt text](images/image-5.png) 
- Run `file out` and I learn that it is: 
![alt text](images/image.png)
- I then run `strings file` which extracts ASCII-printable strings from a given binary and I receive: 
![alt text](images/image-2.png)
- This makes me suspscious that this has to do with a UPX compression. Upon researching on Google, the first Google search I came across was ![alt text](images/image-3.png). A natural reaction is to unpack the UPX packing. 


### Step 2: [Attack]
- First step was installing `upx` via `sudo apt install upx`
- ![alt text](images/image-4.png)
- Referencing the `man` page there was a decompress flag. In order to decompress a file I must conduct `upx -d <file_name>.`
![alt text](images/image-6.png)
- Upon doing this I ran `gdb` and was finally able to see `disass main` and obtain information from `info functions.`


### Step 3: [Third Step Title]
- Continue to describe subsequent steps until the solution is reached. 

### Final Solution/Payload
- Summarize how you arrived at the final solution and any critical insights that helped you solve the challenge.

## Lessons Learned
- Discuss what you learned from the challenge and any techniques or concepts you found particularly interesting.

## References
- Link to any external resources, write-ups, or documentation that were helpful in solving the challenge.

