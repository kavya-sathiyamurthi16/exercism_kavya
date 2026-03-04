"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un"+ word
def make_word_groups(vocab_words):
    return vocab_words[0] + " :: " + " :: ".join([vocab_words[0] + w for w in vocab_words[1:]])

def remove_suffix_ness(word):
    root = word[:-4]
    if root.endswith("i"):
        root = root[:-1] + "y"
    return root

def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index].strip(".")
    return adjective + "en"
