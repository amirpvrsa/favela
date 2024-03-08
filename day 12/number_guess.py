import random
lives=0

GAME_LEVEL=input("choose level game between 'hard' and 'easy' : ")
if GAME_LEVEL=="easy":
    lives=10
elif GAME_LEVEL=="hard":
    lives=5

number=random.randint(1,100)
win=False

while lives>0 and win == False:
    guess = int(input("whats your guess ? : "))
    if guess>number:
        print("Too high !")
        lives-=1
    elif guess<number:
        print("Too low")
        lives-=1
    elif guess==number:
        print("you got it bro")
        win=True
if lives==0:
    print("you are out of lives !!!")