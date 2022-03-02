fruits = ["apple", "banana", "cherry", "banana", "banana", "banana", "banana"]

for x in fruits:
    if x == "banana":
        print("jojo")
if "banana" in fruits:
    print("b")

# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print( "All arguments passed through one parameter" , kids )

my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")