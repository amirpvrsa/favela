height = float(input("Height(in M) : "))
weight = float(input("Weight(in Kg) : "))

bmi= weight/height**2
if bmi <= 18 :
    print(f"your bmi is {bmi}, you are underweight")
elif bmi <= 25 :
    print(f"your bmi is {bmi}, you are normal weight")
elif bmi <= 30 :
    print(f"your bmi is {bmi}, you are slightly overweight")
elif bmi <= 35 :
    print(f"your bmi is {bmi}, you are kiri chaghi")
else:
    print(f"your bmi is {bmi}, you are clinicaly obese")