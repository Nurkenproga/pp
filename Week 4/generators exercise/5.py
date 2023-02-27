#Implement a generator that returns all numbers from (n) down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
        
m = int(input())
for i in countdown(m):
    print(i)