def filter_prime():
    b = 0
    helper = []
    global a
    for i in range(0, len(a)):
        for j in range(1, int(a[i]) + 1):
            if(int(a[i]) % j == 0):
                b = b + 1
        if(b == 2):
            helper.append(a[i])
        b = 0
            
    return helper

a = input().split(' ')
print(filter_prime())