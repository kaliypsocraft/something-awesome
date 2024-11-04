# CTF Write-Up: [Challenge Name][Challenge Type]

## Description
>A brief description of the challenge, including its title, type (e.g., web, crypto, pwn)


## Flag
The flag you obtained after solving the challenge. (e.g., `picoCTF{example_flag}`)

## Difficulty
- **Difficulty Level:** medium

## Tools Used
- List any tools or resources you used to solve the challenge (e.g., Wireshark, Burp Suite, Python, etc.).

## Write-Up

### Preparatory Phase


First, I examined the file using the `file` command but received no information. To gather more details, I used the command `exiftool <file_name>`, which provided valuable insights, revealing that it contained JPEG-like data.

Next, I ran `xxd <file_name>` to obtain a [[hex dump]] of the file. Within the first 20 bytes of a file, the file signature typically resides, indicating the file type. For example, JPEG files usually have a specific signature.
### Attack Phase

The first 4 bytes denoted by `0xe0ffd8ff` appeared to represent the file signature of a JPEG in reverse order, indicating a wrong endian format. To address this issue, I wrote a script that converted the file from little-endian to big-endian.

After running this script, I obtained an output file that contained the flag.
### Final Solution/Payload

NOTE: This script was courtesy of Youtuber [Martin Carlisie](https://www.youtube.com/@carlislemc)
``` py
import struct

def flip_endian(input_file: str, output_file: str, word_size: int = 4):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while chunk := infile.read(word_size):
            if len(chunk) < word_size:
                chunk = chunk.ljust(word_size, b'\x00')
            little_endian_value = struct.unpack('<I', chunk)[0]
            big_endian_value = struct.pack('>I', little_endian_value)
            outfile.write(big_endian_value)

if __name__ == '__main__':
    input_file = 'challengefile'  # Path to your little-endian file
    output_file = 'output_file.jpg'    # Path for the output big-endian file
    convert_endian(input_file, output_file, word_size=4)

```

### Lessons Learnt
- **What are file signatures**
They are usually found in the first 2-4 bytes of a file and identify the format of the file. For example whether it is a `.jpg` or `.bmp` file. They can usually be found via `xxd <filename> | tail`. It can be useful information if there is no vision extension on a file.

## References
- https://en.wikipedia.org/wiki/List_of_file_signatures

