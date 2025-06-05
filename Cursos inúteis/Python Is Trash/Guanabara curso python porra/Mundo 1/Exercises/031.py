kms = float(input('How far is your trip? '))
print(f'You are about to start a journey of {kms}Km.')
if kms <= 200:
    preço = kms * 0.50
else:
    preço = kms * 0.45

print(f'And the price of your ticket will be R${preço:.2f}')