#remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#discard()
thisset1 = {"apple", "banana", "cherry"}
thisset1.discard("banana")
print(thisset1)

#pop()
thisset2 = {"apple", "banana", "cherry"}
x = thisset2.pop()
print(x)
print(thisset2)

#clear()
thisset3 = {"apple", "banana", "cherry"}
thisset3.clear()
print(thisset3)

#del will delete the set completely:
thisset4 = {"apple", "banana", "cherry"}
del thisset4
print(thisset4)