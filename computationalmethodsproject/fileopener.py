# fileopener.py

from xml.etree import ElementTree as ET
import nltk
import string
import collections
import lightlemmatizer
        
def parseXML(filename):
    xml_dict = collections.defaultdict(list)
    tree = ET.parse(filename)
    root = tree.getroot
    for node in tree.iter():
        text = node.text
        tag = node.tag
        text_list = nltk.word_tokenize(text)
        lemmatized_text = lightlemmatizer.lemmatize(text_list)
        for item in lemmatized_text:
            item = ''.join([g for g in item if g not in string.punctuation])
            if item != '':
                xml_dict[tag].append(item.lower())
    # junk for topic modeling
    word_list = []
    for key,value in xml_dict.items():
        if value != ['none'] and key != 'Do_id':
            for word in value:
                word_list.append(word)
    with open('words.txt', 'a') as output:
        output.write(filename + ': ' + ' '.join(word_list) + '\n')
    # end junk for topic modeling
    return xml_dict