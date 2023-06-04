import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


def count_pos_tag(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    verb_count = 0
    noun_count = 0
    pronoun_count = 0
    adjective_count = 0

    for word, tag in pos_tags:
        if tag.startswith('VB'):
            verb_count += 1
        elif tag.startswith('NN'):
            noun_count += 1
        elif tag.startswith('PRP'):
            pronoun_count += 1
        elif tag.startswith('JJ'):
            adjective_count += 1

    pos_counts = {
        'verbs': verb_count,
        'nouns': noun_count,
        'pronouns': pronoun_count,
        'adjectives': adjective_count
    }

    return pos_counts


# Example usage
text = "I want to go outside."
counts = count_pos_tag(text)
print(counts)
