x = 97
y = 0
while y <= 9:
    for i in range(26):
        print("(",y,",",chr(x),")")
        x += 1
    y += 1
    x = 97
