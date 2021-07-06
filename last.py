n=int(input("enter the number"))
f=open("last.text","r")
for line in (f.readlines() [-n]):
    print(line,end="")
f.close()
