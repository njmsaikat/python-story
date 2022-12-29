name = input("Your name:")
salary = float(input("Your salary:"))

commission = round((salary * 13)/100, 2)

print(f"The commission {name} will get is ${commission} as his/her salary is ${salary}")
