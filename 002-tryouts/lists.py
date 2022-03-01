
# #################################################################################
# #################################################################################
mainList= [1,2,3,4,5]
mainList[1:2] = ["here","I","am"]
print(mainList)
secondList= [6,7,8,9]

mainList.extend(secondList)
print(mainList)
mainList.append(10)

a = 2
mainList.insert(a,"I am inserted at {} position".format(a))
print(mainList)

mainList.remove(6) #removes the value given 
print(mainList)
mainList.pop() #removes last ele
print(mainList)
mainList.pop(2) # removes sepcified position
print(mainList)
del mainList[1] # removes sepcified position
print(mainList)
mainList.clear() # removes all values
print(mainList)

# del mainList # deletes list all together
# print(mainList)

# #################################################################################
# #################################################################################
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# #################################################################################
# #################################################################################
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "e" in x or "i" in x]

print(newlist)

# #################################################################################
# #################################################################################
# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
