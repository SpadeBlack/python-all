from pip import main


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