# student_heiights = input().split()
# total_height = 0
# for n in range(0,len(student_heiights)):
#     student_heiights[n]=int(student_heiights[n])
#     total_height += student_heiights[n]
    
# print(f"total heigh = {total_height}")
# print(f"number of srudent is = {len(student_heiights)}")
#######################################################################
# student_score = input().split()
# for n in range (0,len(student_score)):
#     student_score[n]=int(student_score[n])
# highest_score = 0

# for score in student_score:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)
#######################################################################
# total = 0
# for number in range(1,101):
#     total+=number
# print(total)
#######################################################################
# target = int(input("sum of even number from 1 to : ?\n"))
# total = 0
# for number in range(2,target+1,2):
#     total+=number
# print(total)
#######################################################################
# for n in range(1,101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("fizzbuzz")
#     if n % 3 == 0:
#         print("fizz")
#     elif n % 5 == 0:
#         print("buzz")
#     else:
#         print(n)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k','l', 'm', 'n', 'o', 'p', 'a', 'r',
's', 't', 'u', 'v', 'w', 'x','y','z','A','B', 'C', 'D', 'E', 'F','G','H','T','J','K','L', 'M', 'N',
'O', 'P', 'O', 'R','S', 'T', 'U', 'V','W','X','Y', 'z']
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8','9']
symbols = ['!', '#', '$','%','&', '(', ')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many lettèrs would you like in your password?\n"))
nr_symbols = int(input (f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letter=[]
symbol=[]
number=[]
for n in range(0,nr_letters+1):
    rand=random.randint(1,51)
    letter.append(letters[rand])



for n in range(0,nr_numbers+1):
    rand=random.randint(1,9)
    number.append(numbers[rand])
    
for n in range(0,nr_symbols+1):
    rand=random.randint(1,8)
    symbol.append(symbols[rand])
    
# print(symbol,letter,number)

combination = symbol+letter+number
# print(combination)
random.shuffle(combination)
# print(combination)
password = ""
for char in combination:
    password+= char
print(password)
# for n in range(0,len(combination)):



