def is_pangram(sentence):
    sentence = sentence.lower()
    letters = set(char for char in sentence if char.isalpha())
    return len(letters) == 26