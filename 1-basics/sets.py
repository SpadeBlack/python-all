# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Both union() and update() will exclude any duplicate items.

# Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
"""
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	                                Description
add()	                                Adds an element to the set
clear()	                                Removes all the elements from the set
copy()	                                Returns a copy of the set
difference()	                        Returns a set containing the difference between two or more sets
difference_update()	                    Removes the items in this set that are also included in another, specified set
discard()	                            Remove the specified item
intersection()	                        Returns a set, that is the intersection of two other sets
intersection_update()	                Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                        Returns whether two sets have a intersection or not
issubset()	                            Returns whether another set contains this set or not
issuperset()	                        Returns whether this set contains another set or not
pop()	                                Removes an element from the set
remove()	                            Removes the specified element
symmetric_difference()	                Returns a set with the symmetric differences of two sets
symmetric_difference_update()	        inserts the symmetric differences from this set and another
union()	                                Return a set containing the union of sets
update()	                            Update the set with the union of this set and others
"""