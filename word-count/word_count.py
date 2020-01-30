import re
def count_words(sentence):
    bag_of_words = re.findall(r'\w+\'\w+|[a-zA-Z0-9]+', sentence.lower())
    word_frequency = {}
    for word in bag_of_words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1
    return word_frequency
