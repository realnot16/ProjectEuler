c=0
year=1901

def checkFeb(year):
    print("CHECK FEB "+str(year))
    if (year %4 ==0) and (year % 100!=0 or year % 400==0):
        print("BISES")
        return 29
    else:
        return 28


month={ 1:31, 2:0, 3:31,  4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31  }



def checkFirst(year,dCount):
    for m in range (1,13):
        if(m==2):
            month[m]=checkFeb(year)
        if (dCount % 7 ==0):
            print("LA DOMENICA è IL PRIMO NEL MESE "+str(m)+" DELL'ANNO "+str(year))
            global c
            c+=1
        print("aggiungo a "+str(dCount)+" il mese  "+str(m)+" che vale "+str(month[m]))

        dCount+=month[m]
    return dCount

dCount=0
for year in range(1901,2001):
    dCount =checkFirst(year,dCount)



print(c)