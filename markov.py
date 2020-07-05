# Source: https://www.datacamp.com/community/tutorials/markov-chains-python-tutorial

import numpy as np
import random as rm

# The statespace
# Noun
st1 = ["Summer", "Cloud", "Water", "Leaves", "Bird", "Bird", "People"] 
# Verb
st2 = ["Come", "Vanish", "Escape", "Fall", "Sing"]
# Adjective
st3 = ["Blue", "Beautiful", "Fragile", "Green", "Light", "Sweet", "Sweet", "Sweet"]
# Adverb
st4 = ["Quickly", "Dreamingly", "Slowly", "Softly", "Suddenly"]

states = [st1, st2, st3, st4]

# Possible sequences of events
transitionName = [["11", "12", "13", "14"], ["21", "22", "23", "24"], ["31", "32", "33", "34"], ["41", "42", "43", "44"]]

# Probabilities matrix (transition matrix)
pr11 = 0.1
pr12 = 0.6
pr13 = 0.3
pr14 = 0
pr21 = 0.2
pr22 = 0
pr23 = 0.2
pr24 = 0.6
pr31 = 0.9
pr32 = 0
pr33 = 0.1
pr34 = 0
pr41 = 0
pr42 = 0.5
pr43 = 0.5
pr44 = 0
transitionMatrix = [[pr11, pr12, pr13, pr14], [pr21, pr22, pr23, pr24], [pr31, pr32, pr33, pr34], [pr41, pr42, pr43, pr44]]

sumProb = 0
for matrix in transitionMatrix:
    sumProb += sum(matrix)
if sumProb != len(transitionMatrix):
    print("Somewhere, something went wrong. Transition matrix, perhaps?")
else: print("All is gonna be okay, you should move on!! ;)")
# All is gonna be okay, you should move on!! ;)

def getSt(states, change):
    return states[int(change[-1:])-1]

# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    # Choose the starting state
    activityToday = np.random.choice(np.random.choice(states))
    print("Start state: " + activityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [activityToday]
    i = 0
    while i != days:
        if activityToday in st1:
            #print("if st1")
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            activityToday = np.random.choice(getSt(states, change))
            activityList.append(activityToday)
        elif activityToday in st2:
            #print("if st2")
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            activityToday = np.random.choice(getSt(states, change))
            activityList.append(activityToday)
        elif activityToday in st3:
            #print("if st3")
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            activityToday = np.random.choice(getSt(states, change))
            activityList.append(activityToday)
        elif activityToday in st4:
            #print("if st4")
            change = np.random.choice(transitionName[3],replace=True,p=transitionMatrix[3])
            activityToday = np.random.choice(getSt(states, change))
            activityList.append(activityToday)
        i += 1  
        #print("i is: " + str(i))
        #print("current actList: " + str(activityList))
    #print("Possible states: " + str(activityList))
    #print("End state after "+ str(days) + " days: " + activityToday)
    return activityList

# Function that forecasts the possible state for the next 2 days

#activity_forecast(5)


# To save every activityList
list_activity = []

# `Range` starts from the first count up until but excluding the last count
numSen = 4
minLen = 6
maxLen = 10
for iter in range(1, numSen+1):
    list_activity.append(activity_forecast(np.random.randint(minLen,maxLen+1)))

# Check out all the `activityList` we collected    
print(list_activity)


