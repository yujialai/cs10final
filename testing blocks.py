###CS10 FINAL TESTING BLOCK


def test(func, given, output):
    if func(given)==output:
        return True
    else:
        return False

#copy of the actual game function
def howtowincomputer(handvalue): #take in valueonhand,
    liste = []         #return list of wining move[num for com hand, num pl hand]
    for player in range(2,4):
        for comp in range(0,2):
            if handvalue[player] + handvalue[comp] == 5:
                liste.append(int(comp))
                liste.append(int(player))
    return liste

#copy of the actual game function
def createmovenottomake(handvalue): #reporter.take in valueonhand
    resultsofpossiblemoves = []
    computerhand = []
    result = []
    for comp in range(0,2):
        for player in range(2,4):
            if handvalue[player] + handvalue[comp] > 5:
                resultsofpossiblemoves.append(handvalue[player] + handvalue[comp] -5)
            else:
                resultsofpossiblemoves.append(handvalue[player] + handvalue[comp])   
    for comp in range(0,2):
        computerhand.append(handvalue[comp])
    for possibilities in range(0,4):
        for comp in range(0,2):
            if computerhand[comp] + resultsofpossiblemoves[possibilities] == 5:
                if not possibilities+1 in result:
                    result.append(possibilities+1)
    return result

print(test(createmovenottomake,[1, 2, 1, 3],[2, 3]))
print(test(howtowincomputer,[1, 2, 1, 3], [1, 3]))
print(test(createmovenottomake,[1, 2, 1, 2],[2, 3, 4]))
print(test(howtowincomputer,[1, 2, 4, 3], [0, 2, 1, 3]))

