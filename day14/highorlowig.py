import random
import os

from gamedata import data

gamedata=data
random.shuffle(gamedata)
# print(gamedata)
yourscore=0
live=1
while live==1:
    for i in range(1,len(gamedata)-1):
        if live==1:
            print(f"your score is : {yourscore}")
            print(f"Compare A : {gamedata[i]["name"]}, a {gamedata[i]['description']}, from {gamedata[i]['country']}")
            print(f"Compare B : {gamedata[i+1]["name"]}, a {gamedata[i+1]['description']}, from {gamedata[i+1]['country']}")
            print(gamedata[i]['follower_count'])
            print(gamedata[i+1]['follower_count'])
            selected=input("who has more followers? Type A or B").lower()
            
            if selected == "a" and gamedata[i]['follower_count']>gamedata[i+1]['follower_count']:
                print("great job")
                yourscore+=1
                os.system("clear")
            elif selected=="b" and gamedata[i+1]['follower_count']>gamedata[i]['follower_count']:
                print("great job")
                yourscore+=1
                os.system("clear")
            else:
                print("you lost!!")
                live=0
            