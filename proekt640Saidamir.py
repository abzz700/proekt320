def count_vowels(text):
    vowels = "аеёиоуыэюяaeiou"
    return sum(1 for char in text.lower() if char in vowels)