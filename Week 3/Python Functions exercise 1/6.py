def reverse(a):
    n = len(a)
    cnt = 0
    helper = []
    word = ''
    for i in range (0,n + 1):
        if(i == n):
            helper.append(word)
        elif(a[i] != ' '):
            word = word + a[i]
        else:
            helper.append(word)
            word = ''
    
    word = ''
    for i in range(len(helper) - 1, -1, -1):
        word = word + helper[i]
        word = word + ' '

    print(word)

reverse('We are ready')
