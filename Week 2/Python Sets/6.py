#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#update()
thisset1 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset1.update(tropical)

print(thisset1)

#does not have to be a set
thisset2 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset2.update(mylist)

print(thisset2)