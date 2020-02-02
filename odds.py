#odds for superbowl pool
import random
import numpy

#score values
touchdownValue = 7
fieldgoalValue = 3
safetyValue = 2 
touhdownExtraPointValue = 8 

#the "blocks" in our family pool
scoreinthePool = range(0,10) 

numberOfScores = range(0,5) #assumes 4 scores in the frist half is reasoable 
pointsScored = [] #stores simulated points totals for a hypthetical team
simulationnumber = 0 #simulaed first halfs 


while simulationnumber <=100:        
    #generates a random number that will determine what fraction of the scores are TD vs. field goals 
    for score in numberOfScores:
        touchdowns = round(random.random()*score) #rounds to nearest number
        fieldgoals = score-touchdowns
        pointsScored.append(fieldgoalValue*fieldgoals+touchdownValue*touchdowns) #appends the list with a first half score
        #^this could be improved upon be weighting the categories
        
    simulationnumber  +=1


pointsScored = [str(int(i))[-1] for i in pointsScored] #prunes the list to just take the ones digit of any number
poolscore = []
for i in pointsScored:   #creates a matrx of all the ones digits summed 
    for x in pointsScored:
        sum = str(int(x) + int(i))      
        poolscore.append(int(sum[-1])) #because some sums are > 10, this again prunes for ones digits
        
for i in scoreinthePool:
    odds = (poolscore.count(i))/(float(len(poolscore)))*100  #determines the odds that each ones digit will show at half
    print(i,odds)
