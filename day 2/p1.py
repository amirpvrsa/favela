# print("hello"[0])
# # kdskfjksdjbfbkjb
# a = 123

# print(type(a))
# # fstring
# # two // make result int 
# print(11//7)
# a+=1
# print(f"your score is {a}")
print("Welcome to the tip calculator.")
a=float(input("what was the total bill?"))
b=float(input("percentage? 10,12,15 ?"))
c=float(input("beyne chan nafar split beshe ?"))
# print(type(a))

d=(a*((100+b)/100))/c

print(f"each person should pay {round(d,2)}")
