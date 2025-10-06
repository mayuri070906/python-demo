string="Mayuri Chavan"
vowel_set="AEIOUaeiou"
vowels=0
consonants=0
for char in string:
    if char.isalpha():
        if char in vowel_set:
            vowels+=1
        else:
            consonants+=1
print(f"vowels in the string={vowels}")
print(f"consonants in the string={consonants}")
