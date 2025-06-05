num = int(input('Enter a number: '))

unit = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 100

print(f'The unit is {unit}')
print(f'The dezena is {dezena}')
print(f'The centena is {centena}')
print(f'The milhar is {milhar}')


