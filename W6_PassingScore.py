inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
K = int(lines[0])
lines.pop(0)
myScoreList = []
for now in lines:
    x = now.split()
    curManScore = (int(x[-3]), int(x[-2]), int(x[-1]))
    myScoreList.append(curManScore)
print(myScoreList)
goodScoreList = []
for now in myScoreList:
    if now[0] > 39 and now[1] > 39 and now[2] > 39:
        print(now)
        goodScoreList.append(sum(now))
    else:
        continue
goodScoreList.sort(reverse=True)
print(goodScoreList)
if len(goodScoreList) <= K:
        print(0, file=outFile)
else:
    if len(goodScoreList) > K:
        passScore = goodScoreList[K - 1]
        if passScore != goodScoreList[K]:
            print(passScore, file=outFile)
        else:
            print(1, file=outFile)
inFile.close()
outFile.close()
