import nltk
from nltk import pos_tag, word_tokenize

nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')

def timex_distance(t1, t2):
    # Tokenize and part-of-speech tag both temporal expressions
    tokens1 = word_tokenize(t1)
    tokens2 = word_tokenize(t2)

    tagged_tokens1 = pos_tag(tokens1)
    tagged_tokens2 = pos_tag(tokens2)

    # Extract relevant information from the Timex3 tags
    def extract_info(tagged_tokens, offset):
        info = {}
        for token, tag in tagged_tokens:
            if tag.startswith('P'):
                info['presentation'] = int(token[1:])  # presentation XMost timestamp
            elif tag == 'THIS':
                info['this'] = True
            elif tag == 'OFFSET':
                info['offset'] = int(offset)  # offset from the current system time
        return info

    t1_info = extract_info(tagged_tokens1, '+')
    t2_info = extract_info(tagged_tokens2, '-')

    # Compute the distance between the two temporal expressions
    def distance(info1, info2):
        if 'this' in info1 and 'this' in info2:
            return 0.5  # same time reference (THIS)
        elif 'presentation' in info1 and 'presentation' in info2:
            return abs(info1['presentation'] - info2['presentation']) / 1000000  # presentation XMost timestamp difference
        elif 'offset' in info1 and 'offset' in info2:
            return abs(info1['offset'] - info2['offset']) / 1000  # offset difference
        else:
            return 1.0  # unknown or mismatched time references

    distance_value = distance(t1_info, t2_info)

    return distance_value

print(timex_distance(input("First timex3 expression: "), input("Second timex3 expression: ")))
# print(timex_distance("THIS MO", "P1D"))