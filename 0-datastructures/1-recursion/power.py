
def powerOfTwo(n):
    if n == 0:
         return 1
    else:
        power = powerOfTwo(n-1)
        print(power)
        return power * 2

print(powerOfTwo(3))

def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power


print(powerOfTwoIt(4))