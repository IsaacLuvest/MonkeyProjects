import math

angle = float(input('Enter the angle you want: '))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print(f'The angle of {angle:.2f} has the SINE of {sine:.2f}')
print(f'The angle of {angle:.2f} has the COSINE of {cosine:.2f}')
print(f'The angle of {angle:.2f} has the TANGENT of {tangent:2f}')