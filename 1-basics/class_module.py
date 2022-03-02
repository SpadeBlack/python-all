class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def allDetailsWith_KeyArguments(self,**miscellaneous): # ** used for key based arguments 
        try:
            print("Miscellaneous: {},{}".format(miscellaneous["character"],miscellaneous["realName"]))
        except:
            print("No extra information key args")
        return print("All details: {} is {} years old".format(self.name,self.age))
    def allDetailsWith_ListArguments(self,*miscellaneous): # * used for list/array based arguments
        try:
            print("Miscellaneous: {}".format(str(miscellaneous)))
        except:
            print("No extra information list args")
        return print("All details: {} is {} years old".format(self.name,self.age))

p=[]
p.append(Person("John", 36))

p[0].allDetailsWith_KeyArguments( character="fun", realName="Gintama" )
p[0].allDetailsWith_ListArguments( "fun", "Gintama" )

print(len(p))

