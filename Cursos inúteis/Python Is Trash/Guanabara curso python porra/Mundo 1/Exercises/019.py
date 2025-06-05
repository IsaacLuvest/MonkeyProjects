#Choosing a random student
import random

s1 = str(input('First Student: '))
s2 = str(input('Second Student: '))
s3 = str(input('Third Student: '))
s4 = str(input('Fourth Student: '))

random_student = random.choice([s1 , s2, s3, s4])

print(f'The chosen student is: {random_student}.')