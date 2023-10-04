par = open("parells.txt","a")
sen = open("senars.txt","a")

for i in range(1,101):
    if i%2 == 0:
        par.write(str(i)+"\n")
    else:
        sen.write(str(i)+"\n")