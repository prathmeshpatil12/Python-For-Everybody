largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        n = int(num)
        if largest < n:
            largest = n

        if smallest == None or smallest > n:
            smallest = n

    except:
        print
        "Invalid input"
    # print(num)

print("Maximum is", largest)
print("Minimum is", smallest)

#Another way of putting this problem statement in an efficient way.
def largest(a, b):
    if a > b:
        return a
    else if b > a:
        return b
    else:
        return "Both"
largest_No = str(largest(5,6))
if(largest_No == "Both"):
    print("Both the numbers are equal")
else:
    print("Largest number is : ", largest_No)
