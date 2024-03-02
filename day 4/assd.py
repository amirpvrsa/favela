import random
names = input("esme haro vared konid va ba , va space joda konid\n")
name = names.split(", ")

print(name)

name_numbers = len(name)
chosen = name[random.randint(0,name_numbers-1)]

print(chosen + "is goint to pay")