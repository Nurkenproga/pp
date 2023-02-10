def histogram(l):
    helper = ''
    for i in range(0, len(l)):
        for j in range(0, l[i]):
            helper = helper + '*'
        print(helper)
        helper = ''

histogram([4, 9, 7])