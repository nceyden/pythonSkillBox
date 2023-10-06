string = input()

vowels_count = 0
consonants_count = 0

for char in string:
    char = char.lower()  
    if char.isalpha():
        if char in 'аеёиоуыэюя':
            vowels_count += 1
        else:
            consonants_count += 1
            
print(vowels_count, consonants_count)
