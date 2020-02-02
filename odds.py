#odds for superbowl pool
import random
import numpy


touchdownValue = 7
fieldgoalValue = 3
safetyValue = 2 
touhdownExtraPointValue = 8 

scoreinthePool = range(0,10) 
oddsforscoreinthePool = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
numberOfScores = range(0,5) #assumes 4 scores in the frist half is reasoable 
pointsScored = []
n = 0


while n <=1000:
    for score in numberOfScores:
        x = random.random()
        touchdowns = round(x*score)
        fieldgoals = score-touchdowns
        pointsScored.append(fieldgoalValue*fieldgoals+touchdownValue*touchdowns)
        
    n +=1


pointsScored = [str(int(i))[-1] for i in pointsScored]
poolscore = []
for i in pointsScored:
    for x in pointsScored:
        sum = str(int(x) + int(i))
        poolscore.append(int(sum[-1]))
        
for i in scoreinthePool:
    odds = (poolscore.count(i))/(float(len(poolscore)))*100
    print(i,odds)
