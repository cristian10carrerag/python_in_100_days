weight = 80
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underwight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Overweight")