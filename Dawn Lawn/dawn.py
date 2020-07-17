
fr = open("dawn2.txt", "r+")
state = [".", "_", "\\", "-", "/", "|", "*"]
l = []                      #*_/
def flowerFinder():
    flowerCntr = 0
    for k in range(len(l)):
        curState = state.index(l[k])                #curState = state.index('/') = 4
        if curState > 2:                            #4 > 2 --> PASS
            endState = curState + len(l) - i - 3    #endState = 4 + 3 - (-1) - 3 = 5
            if endState >= 6:                       #5 >= 6 --> STOP
                flowerCntr += 1                     #flowerCntr = 0
    return flowerCntr

totFlower = 0
length = len(fr.readlines())   #length = 3
for i in range(-1, length):
    for j in fr.readlines():
        l.append(j[i])
    totFlower += flowerFinder()
    l = []
    fr.seek(0)
print(totFlower)

fr.close()
