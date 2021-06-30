#score = [100, 65, 70, 80, 90]
#sum = 0
#for s in score:
#    sum += s
#print("총점:", sum)
#print("평균:", sum/len(score))


score = [100, 65, 70, 80, 90]
gajung = [0.1, 0.3, 0.2, 0.2, 0.2]
sum = 0
for i in range(len(score)):
    sum += score[i]*gajung[i]
print("총점:", sum)