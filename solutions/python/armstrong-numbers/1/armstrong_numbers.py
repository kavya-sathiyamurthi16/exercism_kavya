def is_armstrong_number(number):
    num_str = str(number)
    power = len(num_str)
    
    total = 0
    for digit in num_str:
        total += int(digit) ** power
    
    return total == number