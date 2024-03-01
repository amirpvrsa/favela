print("i am gonna calculate your love score babyyyyy")
name1 = input("name 1 : ")
name2 = input("name 2 : ")
name = name1 + name2
lowletter_name = name.lower()
# print(lowletter_name)
t = lowletter_name.count("t")
r = lowletter_name.count("r")
u = lowletter_name.count("u")
e = lowletter_name.count("e")
firstdig = t + r + u + e
l = lowletter_name.count("l")
o = lowletter_name.count("o")
v = lowletter_name.count("v")
e = lowletter_name.count("e")
seconddig = l + o + v + e

love_score = int(str(firstdig) + str(seconddig))

if love_score < 10 or love_score > 90:
    print(f"your score is {love_score}, you go together very well")
elif love_score <50 and love_score>40:
    print(f"your score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}, nothing to say")

