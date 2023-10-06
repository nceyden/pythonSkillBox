number = int(input())
if number <= 0:
    print("Неверный ввод"); exit
else:
    bin_number = bin(number)[2:]
    oct_number = oct(number)[2:]
    hex_number = hex(number)[2:]
    
    print(f"{bin_number}, {oct_number}, {hex_number}")
