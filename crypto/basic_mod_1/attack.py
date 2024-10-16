f = open("message.txt", "r")
cipher_text = f.readline()
cipher_text = cipher_text.split()

semi_plain_text = [int(c) % 37 for c in cipher_text]
plain_text = ""

for code in semi_plain_text:
    if 0 <= code and code <= 25:
        plain_text += chr(code + 65)
    elif 26 <= code and code <= 35:
        plain_text += chr(code + 22)
    elif code == 36:
        plain_text += '_'
print(plain_text)
        
    