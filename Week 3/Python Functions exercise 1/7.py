def has_33(nums):
    n = 0
    for i in range(0, len(nums)):
        if(nums[i] == 3):
            n = n + 1
        else:
            n = 0
        if(n >= 2):
            return True

    return False
        

print(has_33([1, 3, 3])) #->True
print(has_33([1, 3, 1, 3])) #->False
print(has_33([3, 1, 3])) #->false  