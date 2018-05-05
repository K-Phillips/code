# bagofwords.py

import collections

def keyword_checker(keywords,word_dict):
    
    occurrences_dict = {}
    
    for key, value in word_dict.items():
        counts_dict = collections.Counter()
        for word in value:
            if word in keywords:
                counts_dict[word] += 1
        if key == 'type':
            occurrences_dict[key] = value
        else:
            occurrences_dict[key] = counts_dict

    return occurrences_dict