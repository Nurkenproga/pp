def solve(numheads, numlegs):
    chickens = 0
    rabbits = 0
    if(numheads < numlegs and numlegs % 2 == 0):
        rabbit = (numlegs - 2 * numheads) / 2
        chicken = numheads - rabbit
    else:
        print('Error')
    return [(chicken), (rabbit)]


print(solve(35,94))