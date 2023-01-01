print("Welcome to the tip calculator")
bill = float(input("What is total bill?\n"))
tip = int(input("How much tip you would like to give? 10, 15, or 20\n"))
people = int(input("How many people to split he bill?\n"))

tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_as_person = total_bill/people
print(f"Each person has to pay {bill_as_person}")


