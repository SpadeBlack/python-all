#### Russian Doll recursive function ###
def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        print("Recurse", doll)
        openRussianDoll(doll-1)

try: 
    openRussianDoll(5)
except:
    print("loll")
