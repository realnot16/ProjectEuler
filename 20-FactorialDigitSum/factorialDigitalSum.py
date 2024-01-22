fact=1
for n in range (1,101):
    fact=fact*n
fact=str(fact)
sum=0
for i in range(0,len(fact)):
    print(fact[i])
    sum+= int(fact[i])

print(sum)