pat=0
grid = 20


#AAA HARD PROGRAMMING SOLUTION - TO SOLVE IT FASTER, DO THE MATH FIRST!

def main():
    move(0,0)
    print(pat)


def move(x,y):
    global pat
    mov=[]
    if (x+1)<grid:
        mov.append([x+1,y])
    if (y+1)<grid:
        mov.append([x,y+1])
    
    for m in mov:
        #print(str(m[0])+" ---- "+str(m[1])+" ------ "+str(pat))
        move(m[0],m[1])
    
    if(x==(grid-1) and y==(grid-1)):
        pat+=1
main()
