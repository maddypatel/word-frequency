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
    """ Takes the string and splits it into list
        Gets the word frequency"""
    word_count = {}
    text = text.split()
    for word in text:
        if word in word_count:
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
        print("{}: {}".format(i[0], i[1]))

if __name__ == "__main__":
    my_string = read_file("sample.txt")
    get_wordfreq = word_frequency(my_string)
    srtdict = sorted_dict(get_wordfreq)
    print_dict(srtdict)
