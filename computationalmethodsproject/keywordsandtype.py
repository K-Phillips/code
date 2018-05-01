# keywordsandtype.py

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
    
    fourteen = ['bile', 'duct', 'cancer', 'cholangiocarcinoma', 'idh1', 'r132h',
                'neuropathy', 'male', 'man', 'sexagenarian', 'adulthood', 'adult']
    fifteen = ['cancer', 'carcinoma', 'cervix', 'cervical', 'female', 'woman',
               'stk11', 'vicenarian', 'young', 'adult']
    twenty = ['liposarcoma', 'mdm2', 'amplification' 'amplify', 'amplified', 'male',
              'vicenarian', 'young', 'adult']
    
    keywords = []
    
    if topic_number == '14':
        keywords = fourteen 
    if topic_number == '15':
        keywords = fifteen
    if topic_number == '20':
        keywords = twenty  
        
    return keywords