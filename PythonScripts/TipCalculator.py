print("Welcome to the tip calculator")

total_bill = float(input("What is the total bill?"))
tip_percent = int(input("what is tip you want to apply? 10 , 12 , 15?"))
num_people = int(input("How Many people will split the bill?"))

final_amount = (total_bill + total_bill * (tip_percent/100))/num_people

print(f"Each person should pay {final_amount}")
print("{:.2f}".format(final_amount))
