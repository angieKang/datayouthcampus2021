def checkPrime(number):
    isPrime = True
    for dividenum in range(2, number):
        remainder = number % dividenum
        if remainder == 0:
            isPrime = False
            break
    return isPrime

def getPrimeNumbers(start, nums):
    result = []
    checkNumber = start
    while True:
        checkResult = checkPrime(checkNumber)
        if checkResult == True: #소수
            result.append(checkNumber)
            if len(result) == nums:
                break
        checkNumber += 1
    print(result)

getPrimeNumbers(2,10)