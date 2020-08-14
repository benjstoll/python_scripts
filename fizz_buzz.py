input_int = input("Please Enter a number: ")
number = int(input_int)

if (number %3 == 0) and (number %5 == 0):
    print("FizzBuzz")
if (number % 3 == 0):
    print("Fizz")
if (number % 5 == 0):
    print("Buzz")
else:
    print(number)

