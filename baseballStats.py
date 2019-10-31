import requests
import pandas as pd
import json

def getPlayerID():
    global active
    global Firstname
    global Lastname
    pIDreponsePart1 = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='"
    pIDreponsePart2 = "'&name_part='"
    pIDreponsePart3 = "%25'"
    active = str(input("Is the player active? (Y or N)\n")).upper()
    Firstname = str(input("What is the players first name? (firstname)\n"))
    Lastname = str(input("What is the players last name? (lastname)\n"))
    pIDresponse = requests.get(pIDreponsePart1 + active + pIDreponsePart2 + Firstname +" " + Lastname + pIDreponsePart3)
    return pIDresponse
    
def userIntStatType(active, Firstname, Lastname):
    print("What would you like to know batting or pitching stats?")
    typeStat = str(input("0 - Batting stats \n1 - Hitting Stats\n"))
    if typeStat == '0':
        pBat = requests.get("http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam?league_list_id=%27mlb%27&game_type=%27R%27&player_id=%27"+pIDresponse.json()['search_player_all']['queryResults']['row']['player_id']+"%27")
        print("What stat would you like to know about?\nSupported Stats\n-------------\n0-Homeruns\n1-Batting Average\n2-RBI\n3-Stolen Bases")
        pBatS = str(input("Input desired stat type\n"))
    
def getPlayerCareerHittingStat(playerID):
    
    
    
    pBat = requests.get("http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam?league_list_id=%27mlb%27&game_type=%27R%27&player_id=%27"+pIDresponse.json()['search_player_all']['queryResults']['row']['player_id']+"%27")
    print("What stat would you like to know about?\nSupported Stats\n-------------\n0-Homeruns\n1-Batting Average\n2-RBI\n3-Stolen Bases")
    pBatS = str(input("Input desired stat type\n"))
    if pBatS == "0":
        return pBat.json()['sport_career_hitting']['queryResults']['row']['hr']
    elif pBatS == "1":
        return pBat.json()['sport_career_hitting']['queryResults']['row']['avg']
    elif pBatS == "2":
        return pBat.json()['sport_career_hitting']['queryResults']['row']['rbi']
    elif pBatS == "3":
        return pBat.json()['sport_career_hitting']['queryResults']['row']['sb']

active = ''
Firstname= ''
Lastname = ''
playerID = ''

print("Please follow proper formating for all API requests. The text within the () will provide instructions for each request.\n")
mode = str(input("Are you going to building a table or just looking for a speific stat?\n0-Looking for player stat\n1-Building a Table\n"))
if mode == '0':
    
    playerID = getPlayerID()
    getPlayerCareerHittingStat(playerID)
    
    







#print(Firstname + " " + Lastname + " has " + str(pBat.json()['sport_career_hitting']['queryResults']['row']['hr']) + " total home runs.")
#print(Firstname + " " + Lastname + " has a batting average of " + str(pBat.json()['sport_career_hitting']['queryResults']['row']['avg']) + " .")
#print(Firstname + " " + Lastname + " has " + str(pBat.json()['sport_career_hitting']['queryResults']['row']['rbi']) + " total runs batted in.")
#print(Firstname + " " + Lastname + " has " + str(pBat.json()['sport_career_hitting']['queryResults']['row']['sb']) + " total stolen bases.")

#active = str(input("Is the player active? (Y or N)\n")).upper()
#Firstname = str(input("What is the players first name? (firstname)\n"))
#Lastname = str(input("What is the players first name? (lastname)\n"))

#http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code=%27mlb%27&active_sw=%27N%27&name_part=%27henderson%25%27
#"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code=%27mlb%27&active_sw=%27"+ active + "name_part=%27" +Firstname+ "%20" + Lastname + "%25%27"
#http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='cespedes%25'
#http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='" + Firstname + " " + Lastname + "%25'
#playerID = playerInfo["player_id"]