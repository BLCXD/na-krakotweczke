x = float(input("Podaj X:"))
y = float(input("Podaj y:"))
z = float(input("Podaj z:"))

if x**2+y**2 == z**2 or z**2 + y**2 == x**2 or x**2 + z**2 == y**2:
    print("trójkąt jest prostokątny")

elif x**2+y**2 < z**2 or z**2 + y**2 < x**2 or x**2 + z**2 < y**2:
    print("trójkąt jest rozwartokątny")

elif x**2+y**2 > z**2 or z**2 + y**2 > x**2 or x**2 + z**2 > y**2:
    print("trójkąt jest ostrokątny")

