
alphabet = {
        'a' : '1', 
        'b' : '2', 
        'c' : '3', 
        'd' : '4', 
        'e' : '5', 
        'f' : '6', 
        'g' : '7', 
        'h' : '8', 
        'i' : '9', 
        'j' : '10', 
        'k' : '11', 
        'l' : '12', 
        'm' : '13', 
        'n' : '14', 
        'o' : '15', 
        'p' : '16', 
        'q' : '17', 
        'r' : '18', 
        's' : '19', 
        't' : '20', 
        'u' : '21', 
        'v' : '22', 
        'w' : '23', 
        'x' : '24', 
        'y' : '25', 
        'z' : '26'
    }

def getPoint(word,position):
    points=0
    for i in word:
        points+=int(alphabet[str(i).lower()])
    return points*int(position)

f = open("0022_names.txt", "r")
words=[]
for x in f:
    words=x.split(",")
for i in range(len(words)):
    words[i]= words[i].replace('"',"")

words.sort()

total=0

for j,w in enumerate(words):
    total+=getPoint(w,j+1)

print(total)