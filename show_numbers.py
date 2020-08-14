def show_numbers(limit):
    for number in range(limit):
        if (number % 2 == 0): print(f"{number} EVEN")
        else: print(f"{number} ODD")

show_numbers(10)
