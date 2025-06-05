from random import randint

random_num = randint(0,5)
print('I will think of an INT number from 0 to 5, guess the number.')
num = int(input('Choose an INT number: '))
if num == random_num:
    print('You guessed the number, congratulations!', random_num)
else:
    print("You didn't get the number right, the number is:" , random_num)