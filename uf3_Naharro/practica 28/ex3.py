f = open('jose.txt', 'r')
a = f.read().split('!')
for i in a:
    i = i.split(':')
    print(i[1],end=' ')