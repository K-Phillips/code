# scoring.py

import collections

def type_checker(count_dict):
    if count_dict['type'] == 'PubMed':
        return pubmed_score(count_dict)
    else:
        return aacr_score(count_dict)

def pubmed_score(count_dict):
    score = 0
    for key,value in count_dict.items():
        if key != 'type':
            positives = set(value)
            if key == 'Doc_title':
                score += len(positives) * 10
            if key == 'Doc_meshdescriptors':
                score += len(positives) * 5
            if key == 'Doc_meshqualifiers':
                score += len(positives) * 3
            if key == 'Doc_abstract':
                score += len(positives) * 2
            if key in ['Doc_ChemicalList','Journal']:
                score += len(positives)
                
    return score
      
def aacr_score(count_dict):
    score = 0
    for key,value in count_dict.items():
        if key != 'type':
            positives = set(value)
            if key == 'Doc_title':
                score += len(positives) * 15
            if key == 'Background':
                score += len(positives) * 2
                
    return score