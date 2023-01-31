#Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#get()
x = thisdict.get("model")
print(x)

#Get Keys
x = thisdict.keys()
print(x)