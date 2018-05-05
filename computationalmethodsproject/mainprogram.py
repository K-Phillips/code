# mainprogram.py
# for file in <directory>/*; do python mainprogram.py "$file" <topicnumber>; done

import sys
import fileopener
import keywordsandtype
import bagofwords
import scoring
import output

def main():
    filename = sys.argv[-2]
    topicnumber = sys.argv[-1]
    word_dict = fileopener.parseXML(filename)
    keywords, typed_word_dict = keywordsandtype.prep_file(word_dict,topicnumber)
    keyword_dict = bagofwords.keyword_checker(keywords,typed_word_dict)
    score = scoring.type_checker(keyword_dict, keywords[:2])
    
    f = open('outfile.txt', 'a')
    f.write(str(filename) + '\t' + str(score) + '\n')

if __name__ == "__main__":
  #Run as main program
  main()