#### Russian Doll recursive function ###

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)


openRussianDoll(4)


# def recursionMethod(parameters):
#     if  exit from condition satisfied:
#         return some value
#     else:
#         recursionMethod(modified parameters)


def firstMethod():
    secondMethod()
    print("I am the first Method")

def secondMethod():
    thirdMethod()
    print("I am the second Method")

def thirdMethod():
    fourthMethod()
    print("I am the third Method")

def fourthMethod():
    print("I am the fourth Method")


firstMethod()


def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else: 
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)
 ## Recursion vs Iterarion###

def powerOfTwo(n):
    if n == 0:
         return 1
    else:
        power = powerOfTwo(n-1)
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

 ## Factorial###


def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


 ## Fibonacci###

def fibonacci(n):
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

#   Created by Elshad Karimov on 4/01/20.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1
def sumofDigits(n):
    assert n>=0 and int(n) == n , 'The number has to be a postive integer only!'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(11111))


#Question 2

def power(base,exp):
    if exp == 0:
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))

print(power(4,2))

# Question 3


def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(12,1.2))

# Question 4
def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(int(n/2))


print(decimalToBinary(1))


