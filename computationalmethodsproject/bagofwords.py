# bagofwords.py

import collections

def keyword_checker(keywords,word_dict):
    
    occurrences_dict = {}
    
    for key, value in word_dict.items():
        counts_dict = collections.Counter()
        for keyword in keywords:
            if keyword in value:
                counts_dict[keyword] += 1
        if key == 'type':
            occurrences_dict[key] = value
        else:
            occurrences_dict[key] = counts_dict
        
    return occurrences_dict