#### Russian Doll recursive function ###
s=0
def openRussianDoll(doll):
    if doll == 0:
        print("All dolls are opened")
    else:
        print("Recurse", doll)
        global s 
        s = s+doll
        openRussianDoll(doll-1)

openRussianDoll(996)
print(s)

