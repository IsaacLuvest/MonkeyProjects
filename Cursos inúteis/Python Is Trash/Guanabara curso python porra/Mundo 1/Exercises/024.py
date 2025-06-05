text = str(input('What city are you from? '))

# Option 1 - tuple (guard-sensitive)
print(text.startswith(("santo", "Santo")))

# Option 2 - lowercase (ignores case)
print(text.lower().startswith("santo"))   # True