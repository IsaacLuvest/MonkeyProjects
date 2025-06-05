import random

s1 = str(input('First Student: '))
s2 = str(input('Second Student: '))
s3 = str(input('Third Student: '))
s4 = str(input('Fourth Student: '))

list = [s1 , s2, s3 , s4] #The brackets
random.shuffle(list)

print('The order of presentation is: ')
print(list)