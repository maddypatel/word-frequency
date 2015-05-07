import re

def read_file(input_file):
    """ Reads the input file and returns a all
        lower case string with all punctuation
        removed"""
    with open(input_file) as file:
        lines = file.read().lower()
        lines = re.sub(r'[\s]+', ' ', lines)
        lines = re.sub(r'[^A-Za-z ]', '', lines)
    return lines

def word_frequency(text):
    """ Takes the string and splits it into list.
        Eliminates common words from the count and
        returns dictionary of word frequency"""
    common_words = ['a','able','about','across','after','all','almost',
                    'also','am','among','an','and','any','are','as','at',
                    'be','because','been','but','by','can','cannot',
                    'could','dear','did','do','does','either','else',
                    'ever','every','for','from','get','got','had','has',
                    'have','he','her','hers','him','his','how','however',
                    'i','if','in','into','is','it','its','just','least',
                    'let','like','likely','may','me','might','most',
                    'must','my','neither','no','nor','not','of','off',
                    'often','on','only','or','other','our','own','rather',
                    'said','say','says','she','should','since','so',
                    'some','than','that','the','their','them','then',
                    'there','these','they','this','tis','to','too','twas',
                    'us','wants','was','we','were','what','when','where',
                    'which','while','who','whom','why','will','with',
                    'would','yet','you','your']
    word_count = {}
    text = text.split()
    for word in text:
        if word in common_words:
            pass
        elif word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def sorted_dict(my_dict):
    """ Sorts the dictionary to top 20 items by values"""
    my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:20]
    return my_dict

def print_dict(my_dict):
    for i in my_dict:
        print("{0:12} {1:100}".format(i[0], int(i[1]/4) * '#'))

if __name__ == "__main__":
    my_string = read_file("sample.txt")
    get_wordfreq = word_frequency(my_string)
    srtdict = sorted_dict(get_wordfreq)
    print_dict(srtdict)
