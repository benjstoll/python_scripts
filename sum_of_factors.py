def number_sum(limit):
    result = 0
    for number in range(limit+1):
        if (number % 3 == 0) or (number % 5 == 0):
            result += number
    return result

print(number_sum(10))

            
