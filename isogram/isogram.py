def is_isogram(string):
    y = string.lower()
    letter_bag = [i for i in y if str.isalpha(i)]
    return len(letter_bag) == len(set(letter_bag))
