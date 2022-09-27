FINAL_AGE = 90
age = int(input("what is your current age"))

years_remaining = FINAL_AGE - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {months_remaining} months, {weeks_remaining} weeks , {years_remaining} years")
