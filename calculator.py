print("********************")
print("*    Calculator    *")
print("********************")

#Input
num_1 = int(input("Enter a first number :"))
num_2 = int(input("Enter a second number :"))

#Choice
print('''
Make a choice:
A. Add
S. Subtract
M. Multiply
D. Divide
''')

#Input choice
ch = input("Enter your choice :")

#Operation
if ch == "A":
    c = num_1 + num_2
    print("Sum is " + f'{c}')
elif ch == "S":
    c = num_1 - num_2
    print("Difference is " + f'{c}')
elif ch == "M":
    c = num_1 * num_2
    print("Product is " + f'{c}')
elif ch == "D":
    c = num_1 // num_2
    print("Quotient is " + f'{c}')
else:
    print("Invalid choice!!!")

#Exit
input("\nPress <ENTER> to quit ...")