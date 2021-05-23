#Write a single function, randInt() that takes up to 2 arguments.
#If no arguments are provided, the function should return a random integer between 0 and 100.
#If only a max number is provided, the function should return a random integer between 0 and the max number.
#If only a min number is provided, the function should return a random integer between the min number and 100
#If both a min and max number are provided, the function should return a random integer between those 2 values.

def randInt(min= 0 , max=  100 ):
    import random
    num = random.random()*(max-min) + min
    return num
print (randInt())
print (randInt(max=50))
print (randInt(min=50))
print (randInt (min=50, max = 500))