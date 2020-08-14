def check_speed(speed):
    if speed <= 74:
        print("Lawful Driver")
        return

    speed = ((speed - (speed % 5)- 70) / 5) 
    points = speed*2

    if points >= 12:
        print("License suspended")
    else:
        print(f"Points: {points}")

check_speed(77)
