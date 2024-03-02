import random
player = input("sang 0, kaghaz 1, ya gheychi 2\n")
list=["sang","kaghaz","gheychi"]
comp = random.randint(0,2)

comb = f"{player}{comp}"
# print(comb)
combination = ["02","10","21","01","12","20","00","11","22"]
place_in_list = combination.index(comb)
# print(place_in_list)
print(f"your choice is {list[int(player)]}")
print(f"pc choice is {list[int(comp)]}")
if place_in_list == 0 or place_in_list == 1 or place_in_list == 2:
    print("dadash bordi tabrik migam")
elif place_in_list == 3 or place_in_list == 4 or place_in_list == 5:
    print("dadash bakhti")
else:
    print("mosavie")