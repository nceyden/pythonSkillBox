a = int(input())
P = round(4 * a, 2)
S = round(a * a, 2)
diagonal = round((2*a**2)**(1/2), 2)

print(f"{P:.2f}, {S:.2f}, {diagonal:.2f}")
