

def sumDiv(n):
    div=[]
    for i in range(1,n):
        if n % i ==0:
            div.append(i)
    sum=0
    for d in div:
        sum+=d
    return sum

sum=0
amicable=[]
for i in range(1,10000):

    amico=sumDiv(i)
    if sumDiv(amico)==i and amico!=i:
        print("coppia trovata "+str(i)+" - "+str(amico))
        if amico not in amicable and i not in amicable:
            amicable.append(amico)
            amicable.append(i)
            sum+= amico+i
print(sum)