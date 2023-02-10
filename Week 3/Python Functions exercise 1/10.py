def unique(l):
    helper = []
    helper.append(l[0])
    for i in range(1, len(l)):
        if(helper.count(l[i]) == 0):
            helper.append(l[i])
        
    return helper


print(unique([1, 2, 3, 1, 2, 3, 5, 3, 2]))
print(unique([1, 'aaa', 'qwerty' , 'aaa', 1 , 4, 2, 2, 4]))   