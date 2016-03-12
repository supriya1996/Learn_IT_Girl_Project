def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
   return x*y
def divide(x, y):
   return x/y

print("Select Operation");
print("1. Addition ");
print("2. Subtraction ");
print("3. Multiplication");
print("4. Division");

choice = input("Enter choice add/subtract/multiply/divide :");

number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))

if(choice == add):
   print(number1, "+", number2, "=", add(number1,number2));

elif(choice == subtract):
   print(number1, "-", number2, "=" subtract(number1,number2));

elif(choice == multiply):
  print(number1, "*", number2, "="  multiply(number1,number2));
  
elif(choice == divide):
   print(number1, "/", number2, "=" divide(number1,number2));
else:
  print("Check Input Properly");
