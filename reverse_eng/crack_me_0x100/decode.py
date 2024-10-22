c = "apijaczhzgtfnyjgrdvqrjbmcurcmjczsvbwgdelvxxxjkyigy"
p = ['' for _ in c]
var_18 = 0x55
var_1c = 0x33
var_20 = 0xf
var_21 = 0x61
rax_10 = 0
rax_16 = 0

for i in range(3):
    for j in range(len(c)):
        rax_10 = (var_18 & (j % 0xff)) + (var_18 & ((j % 0xff) >> 1))
        rax_16 = (var_1c & rax_10) + (var_1c & (rax_10 >> 2))
        normalise_cipher = (ord(c[j]) - 97) % 26
        temp = (normalise_cipher - ((var_20 & rax_16) + (var_20 & (rax_16 >> 4)))) % 26
        p[j] = chr(temp + 97)
    c = ''.join(p)

print(c)