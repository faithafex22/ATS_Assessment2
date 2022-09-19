#Write a program that takes a word and returns the number of consonants and vowels in
# that word.

def count(word):
    vowels_count = 0
    consonants_count = 0
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    for i in word:
        if i.lower() in vowels:
            vowels_count += 1
        elif i.lower() in consonants:
            consonants_count += 1
        else:
            continue
    return f'total number of vowels is {vowels_count} and total number of consonants is {consonants_count}'
        
print(count("@gmail.com"))
        