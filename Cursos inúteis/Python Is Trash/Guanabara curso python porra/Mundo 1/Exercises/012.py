price = float(input('What is the original product price? R$: '))

discount = price * 5 / 100
final = price - discount

print(f'The product that cost R${price:.2f}, with a 5% discount is R${final:.2f} ')