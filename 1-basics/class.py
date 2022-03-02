class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def allDetailsWith_KeyArguments(self,**miscellaneous): # ** used for key based arguments 
        try:
            print("Miscellaneous: {},{}".format(miscellaneous["character"],miscellaneous["realName"]))
        except:
            print("No extra information")
        return print("All details: {} is {} years old".format(self.name,self.age))
    def allDetailsWith_ListArguments(self,*miscellaneous): # * used for list/array based arguments
        try:
            print("Miscellaneous: {},{}".format(miscellaneous[0],miscellaneous[1]))
        except:
            print("No extra information")
        return print("All details: {} is {} years old".format(self.name,self.age))


p1 = Person("John", 36)

p1.allDetailsWith_KeyArguments( character="fun", realName="Gintama" )
p1.allDetailsWith_ListArguments( "fun", "Gintama" )

