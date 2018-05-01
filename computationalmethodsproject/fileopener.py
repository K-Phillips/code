# fileopener.py

from xml.etree import ElementTree as ET
import nltk
import string
import collections
        
def parseXML(filename):
    xml_dict = collections.defaultdict(list)
    tree = ET.parse(filename)
    root = tree.getroot
    for node in tree.iter():
        text = node.text
        tag = node.tag
        text_list = nltk.word_tokenize(text)
        for item in text_list:
            item = ''.join([g for g in item if g not in string.punctuation])
            if item != '':
                xml_dict[tag].append(item.lower())

    return xml_dict