# scoring.py

import collections

def type_checker(count_dict, top_keywords):
    if count_dict['type'] == 'PubMed':
        return pubmed_score(count_dict, set(top_keywords))
    else:
        return aacr_score(count_dict, set(top_keywords))

def pubmed_score(count_dict, top_keywords):
    score = 0
    for key,value in count_dict.items():
        if key != 'type':
            for word in top_keywords:
                if word in value:
                    score += value[word] * 3
            positives = set(value)
            if key == 'Doc_title':
                score += len(positives) * 25
                score += len(set(value).intersection(top_keywords)) * 10
            if key == 'Doc_meshdescriptors':
                score += len(positives) * 8
                score += len(set(value).intersection(top_keywords)) * 2
            if key == 'Doc_meshqualifiers':
                score += len(positives) * 3
                score += len(set(value).intersection(top_keywords)) * 2
            if key == 'Doc_abstract':
                score += len(positives) * 2
                score += len(set(value).intersection(top_keywords)) * 2
            if key in ['Doc_ChemicalList','Journal']:
                score += len(positives)
                score += len(set(value).intersection(top_keywords)) * 2
                
    return score
      
def aacr_score(count_dict, top_keywords):
    score = 0
    for key,value in count_dict.items():
        if key != 'type':
            for word in top_keywords:
                if word in value:
                    score += value[word] * 3
            positives = set(value)
            if key == 'Doc_title':
                score += len(positives) * 25
                score += len(set(value).intersection(top_keywords)) * 10
            if key == 'Background':
                score += len(positives) * 12
                score += len(set(value).intersection(top_keywords)) * 2
                
    return score