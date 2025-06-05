n1 = str(input('Type your name: '))
print('Analyzing your name...')
print('Your name in capital letters is', n1.upper())
print('Your name in lowercase letters is', n1.lower())
print('Number of letters in your name is', sum(1 for c in n1 if c.isalpha()))

phrase = n1.split()[0]
letter = sum(1 for c in phrase if c.isalpha())

print(f'His first name is {phrase} and he has {letter} letters')