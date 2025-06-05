Large = float(input('Wall Width: '))
Height = float(input('Wall Height: '))

area = Large * Height
paint = area / 2

print(f'Your wall has a dimension of {Large}x{Height} and its area is {area:.2f}m²')
print(f'And to paint this wall you will need {paint:.2f}L of Ink')