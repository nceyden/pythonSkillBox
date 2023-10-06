string = input()
odd_sum = 0
even_sum = 0
for i in range(len(string)):
    if (i % 2) == 0:
        even_sum += int(string[i])
    else:
        odd_sum += int(string[i])
if (((even_sum + odd_sum*3) % 10) == 0):
    print("yes")
else: print("no")