Meters = float(input('Say a distance in meters: '))

km = Meters / 1000
hm = Meters / 100
dam = Meters / 10
dm = Meters * 10
cm = Meters * 100
mm = Meters * 1000

print(f"{Meters} in km is {km:.3f}")
print(f"{Meters} in hm is {hm:.2f}")
print(f"{Meters} in dam is {dam:.1f}")
print(f"{Meters} in dm is {dm:.0f}")
print(f"{Meters} in cm is {cm:.0f}")
print(f"{Meters} in mm is {mm:.0f}")

