import random


upperbound= 99
lowerbound = 0
answer = random.randrange(lowerbound, upperbound+1)
a = random.randrange(lowerbound, upperbound+1)

while True:
    if a < answer:
        print(a, ": up")
        lowerbound = a
        a = random.randrange(lowerbound, upperbound)
    elif a > answer:
        print(a, ": down")
        upperbound = a
        a = random.randrange(lowerbound, upperbound)
    elif a == answer:
        print("ding-dong answer is", answer)
        break