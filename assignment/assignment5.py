import random as rand
import datetime as dt
# 1) Import the random function and generate both a random number between 0 and 1
# as well as a random number between 1 and 10.
 
print(rand.random())
print(rand.randint(1, 10))
 
# 2) Use the datetime library together with the random number to generate a random, unique value.
 
x = dt.datetime(2018, 5, 5).strftime('%j')
print(rand.uniform(0, int(x)))

currentTime=dt.datetime.now()

randomValue=rand.uniform(0,100)



print('{:3.2f} has generated randomly at the time of {}'.\

format(randomValue,currentTime))