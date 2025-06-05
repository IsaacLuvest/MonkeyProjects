days = int(input('How many days was the car rented? '))
kms = float(input('How many Kms was the car rented? '))

days_rented = days * 60
kms_rented = kms * 0.15
full_payment = days_rented + kms_rented

print(f'The total for payment is R${full_payment:.2f}')