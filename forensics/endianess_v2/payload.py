import struct

def convert_endian(input_file: str, output_file: str, word_size: int = 4):
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
