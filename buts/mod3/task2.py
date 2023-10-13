try: n = int(input()); print(bin(n)[2:], oct(n)[2:], hex(n)[2:]) if (n >= 0) else print("Неверный ввод")
except: print("Неверный ввод")
