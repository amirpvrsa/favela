year = int(input(" Enter the year i will tell you if its leap or not :"))

if year % 4 != 0 :
    print("it is not leap!!!")
else:
    if year % 100 != 0:
        print("it is a leap year")
    else:
        if year % 400 == 0 :
            print("it is a leap year")
        else:
            print("it is not a leap year")
