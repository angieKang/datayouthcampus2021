import random

def makenum():
    answer = []
    while len(answer) < 4:
        num = random.randint(1,9)
        if num not in answer:
            answer.append(num)
    return answer

def judgestrike(useranswer,answer):
    strikenum = 0
    for i in range(len(useranswer)):
        if useranswer[i] == answer[i]:
            strikenum += 1
    print("strike 개수 :", strikenum)
    return strikenum


def judgeball(useranswer,answer):
    ballnum =0
    for i in range(len(useranswer)):
        ballnum += useranswer.count(answer[i-1])
    print("ball 개수 :", ballnum)
    return ballnum




#main
answer = makenum()
while True:
    user = input("네자리 수(중복된 숫자X)입력 또는 정답을 보시려면 0000을 입력하세요.\n ")

    if int(user) == 0000:
        a = 0
        for i in range(len(answer)):
            a += answer[i]*10**(len(answer)-i-1)
        print(a)
    else:
        useranswer = list(map(int, str(user)))
        judgeball(useranswer,answer)
        if judgestrike(useranswer,answer) == 4:
            print("정답입니다!")
            break