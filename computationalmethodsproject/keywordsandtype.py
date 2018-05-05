# keywordsandtype.py
import lightlemmatizer

def prep_file(word_dict,topic_number):
    
    keywords = get_keywords(topic_number)
    
    keylist = []
    [keylist.append(key) for key in word_dict.keys()]    
    word_dict['type'] = get_doctype(word_dict)
    
    return keywords, word_dict

    
def get_doctype(keys):
    
    doctype = 'PubMed'
    
    for key in keys:
        if key == 'Background':
            doctype = 'AACR'
            
    return doctype

    
def get_keywords(topic_number):
    
    fourteen = ['cholangiocarcinoma', 'duct', 'bile', 'cancer', 'idh1', 'r132h',
                'neuropathy', 'male', 'man', 'adulthood', 'adult', 'biliary']
    fifteen = ['cervix', 'cervical', 'cancer', 'carcinoma', 'stk11', 'young', 
               'adult']
    # for topic 20, We've had to add 'liposarcomas' (plural) to the keyword list because
    # a standard lemmatizer does not handle the "as" ending correctly as a plural for 
    # obvious reasons... "has", "was", "whereas", etc.
    twenty = ['liposarcoma', 'soft', 'liposarcomas', 'amplification', 'amplify', 'amplified', 'male',
              'young', 'adult']
    
    keywords = []
    
    if topic_number == '14':
        keywords = lightlemmatizer.lemmatize(fourteen)
    if topic_number == '15':
        keywords = lightlemmatizer.lemmatize(fifteen)
    if topic_number == '20':
        keywords = lightlemmatizer.lemmatize(twenty)
        
    return keywords