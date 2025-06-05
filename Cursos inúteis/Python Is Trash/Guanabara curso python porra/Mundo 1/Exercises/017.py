import math

opposite = float(input('Type the Length of the opposite leg: '))
adjacent = float(input('Type the Length the adjacent cathetus: '))
hypotenuse = math.hypot(opposite, adjacent)

print(f'The hypotenuse will measure {hypotenuse:.2f}')