f = open("triangle.txt", "r")

triangle=[]
for x in f:
    x=x.split("\n")[0]
    row=x.split(" ")
    triangle.append(row)

tCopy=triangle.copy()
for y in reversed(range(0,len(triangle)-1)):
    for i,x in enumerate(triangle[y]):
        if tCopy[y+1][i]> tCopy[y+1][i+1]:
            tCopy[y][i] = int(tCopy[y][i])+int(tCopy[y+1][i])
        else:
            tCopy[y][i] = int(tCopy[y][i])+int(tCopy[y+1][i+1])
print(tCopy[0][0])