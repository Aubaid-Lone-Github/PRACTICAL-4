num = list(input("Enter a binary number: "))
rem = 0

for i in range(len(num)):
    digit = num.pop()
    if digit == '1':
        rem = rem+pow(2, i)
print("The decimal value of number is : ",rem)        