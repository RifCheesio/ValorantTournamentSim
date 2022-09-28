
from itertools import count
import random

from numpy import place
from teams import Teams




DRX = Teams("DRX", "Korea")
OG = Teams("Optic Gaming", "NA")
XSET = Teams("XSET", "NA")
HThieves = Teams("100 Thieves", "NA")
Leviatan = Teams("Leviatan", "LATAM")
LOUD = Teams("Loud", "Brazil")
FNC = Teams("Fnatic", "EMEA")
TLiq = Teams("Team Liquid", "EMEA")
FPX = Teams("FunPlus Phoenix", "EMEA")
PRX = Teams("PaperRex", "APAC")
XER = Teams("Xerxia", "APAC")
EDG = Teams("Edward Gaming", "China")
ZETA = Teams("Zeta Divison", "Japan")
BOOM = Teams("Boom Esports", "APAC")
KRU = Teams("KRU Esports", "SA")
FUR = Teams("FURIA", "SA")

currentTeams = [DRX, OG, XSET, HThieves, Leviatan, LOUD, FNC, TLiq, FPX, PRX, XER, EDG, ZETA, BOOM, FUR, KRU]


teamsPlayed = []

winningTeams = []
eliminatedTeams = []

matchPlayed = []

tourneyRound = 1
roundToPlay = 1

tournamentBeingPlayed = True

def get_team(listOfTeams):

    teamPosition = random.randint(0, totalTeams -1)
    chosenTeam = listOfTeams[teamPosition]

    return chosenTeam

def clear_history(listToClear):
    i = 0
    while (len(listToClear)!=0):
        listToClear.remove(listToClear[0])

def play_match(match):
    winner = random.randint(0,1)
    for team in match:
        if team == match[winner]:
            winningTeams.append(team)
        else:
            eliminatedTeams.append(team)

    clear_history(match)


while (tournamentBeingPlayed):
    while (len(currentTeams) != 0 and tourneyRound == roundToPlay):
        totalTeams = len(currentTeams)-1

        team1 = get_team(currentTeams)
        currentTeams.remove(team1)

        team2 = get_team(currentTeams)
        currentTeams.remove(team2)

        teamsPlayed.append(team1)
        teamsPlayed.append(team2)

        matchPlayed.append(team1)
        matchPlayed.append(team2)
        play_match(matchPlayed)



    if (len(currentTeams) == 0):

        for team in winningTeams:
            currentTeams.append(team)
        
        print('----------------------')
        
        if tourneyRound == 1:
            placements = 'Teams that placed 8-16th'
        elif tourneyRound == 2:
            placements = 'Teams that placed 4-7th'
        elif tourneyRound == 3:
            placements = 'Teams that placed 2nd and 3rd'
        elif tourneyRound == 4:
            placements = 'Winners'
            tournamentBeingPlayed = False


        roundToPlay += 1
        tourneyRound += 1

        clear_history(winningTeams)

        print(placements)
        for team in eliminatedTeams:
            print(team.name + ' | ' + team.country)
        clear_history(eliminatedTeams)

        print('----------------------')







