f = open("0102_triangles.txt", "r")
triangles=[]
for x in f:
    coord=[]
    x=x.split("\n")[0]
    x= x.split(",")
    coord.append([x[0],x[1]])
    coord.append([x[2],x[3]])
    coord.append([x[4],x[5]])
    triangles.append(coord)

print(triangles)




def checkOrigin(tris):
    # (x1(y2-y3)+x2(y3-y1)+x3(y1-y2))/2
    
    x=0
    y=0
    area=(int(tris[0][0])*(int(tris[1][1])-int(tris[2][1]))+int(tris[1][0])*(int(tris[2][1])-int(tris[0][1]))+int(tris[2][0])*(int(tris[0][1])-int(tris[1][1])))/2
    a1=(x*(int(tris[1][1])-int(tris[2][1]))+int(tris[1][0])*(int(tris[2][1]))+int(tris[2][0])*(-int(tris[1][1])))/2
    a2=(int(tris[0][0])*(y-int(tris[2][1]))+x*(int(tris[2][1])-int(tris[0][1]))+int(tris[2][0])*(int(tris[0][1])-y))/2
    a3=(int(tris[0][0])*(int(tris[1][1])-y)+int(tris[1][0])*(y-int(tris[0][1]))+x*(int(tris[0][1])-int(tris[1][1])))/2

    if(area==(a1+a2+a3)):
        print("origine inside")

c=0
for tris in triangles:
    checkOrigin(tris)
    c+=1
print(c)