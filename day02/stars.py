def printDan(dan, n):
    print("구구단", dan, "단을 출력합니다.")
    for i in range(2, int(n+1)):
        print(dan, "x", i, "=", dan*i)
printDan(5, 18)