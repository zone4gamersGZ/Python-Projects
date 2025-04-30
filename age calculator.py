import datetime

current_year= datetime.datetime.now().year

birth_year = int(input("What year were you born in?"))

age = current_year - birth_year

print(f"You are {age} years old")