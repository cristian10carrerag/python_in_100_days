print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
percent = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

""" total = ((bill * percent / 100) + bill) / people """
total = round(((1 + percent / 100) * bill) / people, 2)

print(f"each person should pay ${total}")

