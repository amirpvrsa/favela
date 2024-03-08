import random




cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def cardpick_user():
    return cards[random.randint(0,12)]


# def cardpick_pc():
#     pc_card=[]
#     pc_card.append(cards[random.randint(0,12)])
#     return pc_card

wanna_play = input("do you wanna play ? type y/n : ")

while wanna_play =="y":
    p=[cardpick_user(),cardpick_user()]
    sum_p = 0
    for l in p:
        sum_p += l
    print(f"your cards : {p}, current score : {sum_p}")
    c = [cardpick_user()]
    pc_sum=c[0]
    game=True
    print(f"computer's first card : {c}")
    while sum_p<21 and game==True:
        hit_stay= input("Type 'y' to get another card and 'n' to stay on this hand : ")
        if hit_stay == "y":
            p.append(cardpick_user())
            sum_p = 0
            for l in p:
                sum_p += l
            print(f"your cards : {p}, current score : {sum_p}")
        else:
            c.append(cardpick_user())
            game=False
            pc_sum=0
            for l in c:
                pc_sum+=l
            while pc_sum<17:
                c.append(cardpick_user())
                pc_sum += c[len(c)-1]
            print(f"your cards : {p}, current score : {sum_p}")
    
    if sum_p>21:
        print(f"pc= {c}")
        print(f"you = {p}")
        print("you lose.")
    elif sum_p>pc_sum:
        print(f"pc= {c}")
        print(f"you = {p}")
        print("you won.")
    elif pc_sum>sum_p and pc_sum<21:
        print(f"pc= {c}")
        print(f"you = {p}")
        print("you loose.")
    elif pc_sum>21:
        print(f"pc= {c}")
        print(f"you = {p}")
        print("you won.")
    elif pc_sum==sum_p:
        rint(f"pc= {c}")
        print(f"you = {p}")
        print("draw.")
    wanna_play = input("do you wanna play ? type y/n : ")   