
with open("day4/input") as w:
    r= w.readlines()

# list of l[row][column] accessed letters
letterwise = [[l for l in s] for s in r]

def adjacent(row,column):
    bran = dict()
    bran["left"] = (row, column-1)
    bran["right"] = (row, column+1)
    bran["up"] = (row+1, column)
    bran["down"] = (row-1, column)
    bran["dupl"] = (row+1, column-1)
    bran["dupr"] = (row+1, column+1)
    bran["dlol"] = (row-1, column-1)
    bran["dlor"] = (row-1, column+1)
    return bran
count = 0 
for i in range(len(letterwise)):
    for j in range(len(letterwise[i])):
        if letterwise[i][j] == "X":
            for pos in ["left","right","up","down","dupl","dupr","dlol","dlor"]:
                row = i
                col = j
                ll = []
                try:
                    for _ in range(3):
                        row,col = adjacent(row,col)[pos]

                        if not ((0<=row<=len(letterwise)) and (0<=col<=len(letterwise[i]))):
                            continue
                        
                        ll.append(letterwise[row][col])
                except:
                    continue
                if ll == ["M","A","S"]:
                    count+=1

print(count)
count=0
for i in range(len(letterwise)):
    for j in range(len(letterwise[i])):
        if letterwise[i][j] == "A":
            ll = []
            for pos in ["dupl","dupr","dlol","dlor"]:
                row = i
                col = j
                # ll = []
                try:
                    
                    row,col = adjacent(row,col)[pos]

                    if not ((0<=row<=len(letterwise)) and (0<=col<=len(letterwise[i]))):
                        continue
                    
                    ll.append(letterwise[row][col])
                except Exception as E:
                    continue
                if len(ll)==4 and set(ll) == set(["M","S"]) :
                    dupl, dupr, dlol, dlor = ll
                    if dupl != dlor and dupr != dlol:
                        count += 1


                    

print(count)