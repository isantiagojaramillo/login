password = "admin";

pssw = input("Enter password: ").lower();

if pssw != password:
  print("wrong password");
else:
  print("Welcome!");

menu = "Menu\n";
menu += "1. Addition\n";
menu += "2. Substraction\n";
menu += "3. Multiplication\n";
menu += "4. Division\n";

try:
  option = int(input("Enter an option: "+menu));
except:
  print("The value can not be a string");



if option == 1:
  try:
    number1 = int(input("Enter first number: "));
    number2 = int(input("Enter second number: "));
  except:
    print("The values can not be strings");
  result = number1 + number2;
  print(result);
elif option == 2:
  try:
    number1 = int(input("Enter first number: "));
    number2 = int(input("Enter second number: "));
  except:
    print("The values can not be strings");
  result = number1 - number2;
  print(result);
elif option == 3:
  try:
    number1 = int(input("Enter first number: "));
    number2 = int(input("Enter second number: "));
  except:
    print("The values can not be strings");
  result = number1 * number2;
  print(result);
elif option == 4:
  try:
    number1 = int(input("Enter first number: "));
    number2 = int(input("Enter second number: "));
    result = number1 / number2;
    print(result);
  except:
    print("The values can not be strings");
    print("Divison by 0 occurred");

else:
  print("Invalid option");