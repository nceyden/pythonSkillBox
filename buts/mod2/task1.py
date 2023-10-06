numbers = input()

comma_index = numbers.index(',')
a_str = numbers[:comma_index]
b_str = numbers[comma_index + 1:]

a = int(a_str)
b = int(b_str)

remainder = a % b

print(remainder)