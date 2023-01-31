#Remove Items
#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
thistuple1 = ("apple", "banana", "cherry")
y = list(thistuple1)
y.remove("apple")
thistuple1 = tuple(y)

#del The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists