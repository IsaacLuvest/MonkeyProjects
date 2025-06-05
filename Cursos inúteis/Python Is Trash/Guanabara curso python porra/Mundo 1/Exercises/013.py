salary = float(input("What is the employee's salary? R$: "))

increase = salary * 0.15
new_salary = increase + salary

print(f'An employee who earned R${salary:.2f}, with a 15% increase, now receives R${new_salary:.2f}.')