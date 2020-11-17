# This first line is provided for you

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = float(input("Enter rate:"))
pay = hrs*rate
print("Pay: ",pay)

#Input options for multiple input using split()
hrs1 = input("Enter 5 numbers:")
list_hrs1 = list(map(float, hrs1.split(" ")))
print(list_hrs1)
