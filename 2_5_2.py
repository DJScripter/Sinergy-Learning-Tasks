word = input("Введите слово из маленьких латинских букв: ")

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonant_count = 0
vowel_count = 0

for char in word:
    if char in vowels:
        vowels[char] += 1
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print(f"Гласных букв: {vowel_count}")
print(f"Согласных букв: {consonant_count}")
print("\nКоличество каждой гласной буквы:")
for vowel, count in vowels.items():
    if count == 0:
        print(f"{vowel}: False")
    else:
        print(f"{vowel}: {count}")
