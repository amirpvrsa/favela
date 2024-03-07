mikhad_bezane=True
dic={}
while mikhad_bezane==True:
    key=input("what is your name ghorbonet beram?").lower()
    value=float(input("how much you wanna bid? $"))
    dic[key]=value
    jigili=input("is there anyone left to bid ? type yes, if not type no.\n")
    if jigili=="no":
        mikhad_bezane=False
# print(dic)
b=0
c=""
for n in dic:
    if dic[n]>b:
        b=dic[n]
        c=n
print(f"winner is {c}. Bid was {b}")