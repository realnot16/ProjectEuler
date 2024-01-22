n=[]


f = open("file.txt", "r")

sum=0
for x in f:
    x=x.split("\n")[0]
    sum+= int(x)
print(str(sum)[:10])