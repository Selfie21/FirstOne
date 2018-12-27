import time

operation = input("What operation would you like to perform?")
print("okay i will " + operation + " 2 numbers")
num1 = input("what is your first number?")
num2 = input("what will be your second number?")

print("thank you for your input... Your result will be with us shortly")
time.sleep(2)
print("Here are your results: ")
time.sleep(0.5)
print( float(num1) + float(num2))