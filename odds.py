####odds for superbowl pool####

#my family started a super bowl pool and assigned everyone an integer from 0 to 9. 
#the ones digit of the scores are summed at half time and the end of the game. whoever has the sum of those digits wins big
#NOTE if the sum is >9, its again taken as the ones digit 28 to 28 yields 16 (8+8), and the winner is 6 

import random

def oddsgenerator(ActualScore1, ActualScore2,maxnumberofscores,initsimulationnumber):
    #football score values
    touchdownValue = 7
    fieldgoalValue = 3
    safetyValue = 2 #currently unintegrated 
    touhcdownExtraPointValue = 8 
    touchdownMissedFgValue = 6 #currently unintegrated

    #the "blocks" in our family pool, the int you get assigned 
    scoreinthePool = range(0,10) 

    numberOfScores = range(0,maxnumberofscores) #makes a list of possible scoring incident numbers (aka 3 TDs + 1 FG = 4)
    pointsScored = [] #stores simulated points totals for a hypthetical team
    
    simulationnumber = initsimulationnumber #preserves the simulatiom number for output because simulationnumber is decremented to 0 

    while simulationnumber >=0:         
        #two point conversion happens ~1% of the time, with a ~35% success rate lets call it .3% percent of scores are 2ptcv
        #for every score roll a 1:300 dice. if its 1, then add a TDw/ extra point and leave one less score to be divvied up between 
        #a regular TD and FG
        #then generate a random fraction that will determine what of the remaining scores are TD. weighted for TD frequency (66% of scores per NFL)

        for score in numberOfScores:
            testfortwopt = random.randrange(0,300)
            touchdownExtraPoint = 0
            iterator = score    #pass score to 'iterator' which checks every score for a 2pt conversion
            while iterator !=0:
                if testfortwopt ==1:
                    touchdownExtraPoint +=1
                    score = score-touchdownExtraPoint #makes one less score available for standard TD and FG
                iterator -=1

            touchdowns = round(random.random()*score)+(0.6) #.6 is weighting based on NFL frequency 
            fieldgoals = score-(touchdowns) 
            teamselector = 0  #once the game starts, its possible to update the model based on previous scores
            #use team selector flag to add the generated points to the already exisiting score of team 1 or 2
            if teamselector%2 ==0:  #even odd gate 
                #team one gets the points 
                pointsScored.append(ActualScore1 + fieldgoalValue*fieldgoals+touchdownValue*touchdowns+touchdownExtraPoint*touhcdownExtraPointValue) #appends the list with a first half score
            else:
                #team two gets the points
                pointsScored.append(ActualScore2 + fieldgoalValue*fieldgoals+touchdownValue*touchdowns+touchdownExtraPoint*touhcdownExtraPointValue)
            touchdownExtraPoint = 0
            teamselector +=1
        simulationnumber  -=1


    pointsScored = [str(int(i))[-1] for i in pointsScored] #prunes the list to just take the ones digit of any number
    poolscore = [] #empty list that will get all the possible outcomes from the simulations 
    for i in pointsScored:   #creates a matrx of all the ones digits summed with each other
        for x in pointsScored:  #these steps are slowwwwww. Rate limiting for sure. probably a faster way to mesh the list
            sum = str(int(x) + int(i))      
            poolscore.append(int(sum[-1])) #because some sums are > 10, this again prunes for ones digits
    print('actual score 1:', ActualScore1)
    print('actual score 2:', ActualScore2)
    print('simulated games', initsimulationnumber)
    print('range high end of points per team',maxnumberofscores)       
    for i in scoreinthePool:
        odds = (poolscore.count(i))/(float(len(poolscore)))*100  #determines the odds that each ones digit will show at half
        
        print(i,odds)

#added user input command line interface that accounts for exisiting scores 
scoreteam1 = input('score of team 1:')
scoreteam2 = input('score of team 2:')
expectedscores = input('high end of expected scoring incidents:')
simulationnum = input('number of simulations you would like to run:')

oddsgenerator(scoreteam1,scoreteam2,expectedscores,simulationnum)

