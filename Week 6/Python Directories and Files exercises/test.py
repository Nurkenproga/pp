def function():
    for i in range(5, 10):
        yield i
        
        
with open("P.txt" , "w") as f:
    for i in function():
      f.write(str(i))
    

        