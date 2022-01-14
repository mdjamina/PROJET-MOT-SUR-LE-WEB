#!/usr/bin/python
import sys, getopt
from konlpy.tag import Okt
import codecs
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



def tokenize(text,lang='fr'):
    """
    https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1
    """    
    #Initialize the class as an object
    if lang in ['ja','as','ko','ks','zh']:
        okt=Okt()
        return okt.morphs(text.replace('\n',' '))

    return word_tokenize(text)

    

def set_getops(argv):
    global input_file
    global process

    input_file=""
    process=""

    try:
        opts, args = getopt.getopt(argv,"hi:g:l:",["in_file=","get=","lang="])

    except getopt.GetoptError:
      print('script.py -i <inputfile> -g <index/bigrams> -l <lang>')
      sys.exit(2)
    
    for opt, arg in opts:
      if opt == '-h':
         print('script.py -i <input_file> -g <index/bigrams>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         input_file = arg
      elif opt in ("-g", "--get"):
         process = arg
      elif opt in ("-l", "--lang"):
         lang = arg


def read_file(file_path):
    with open(file_path,'r',encoding="utf-8", errors='replace') as file :
        return file.read()

def get_frequency(tokens, reverse=True):
    return sorted(set([(tokens.count(i),i) for i in tokens]), reverse=reverse)

def make_bigrams(words):
    return [(i,j) for (i,j) in zip(*[words[i:] for i in range(2)])]

def main(argv):

    set_getops(argv)
    #print(input_file)
    text = read_file(input_file)

    words = tokenize(text)

    if process=='index':
        #print('-----------------')
        for (f,w) in get_frequency(words):
            print('{0}\t{1}'.format(f,w))
    elif process=='bigrams':
        for (w1,w2) in make_bigrams(words):
            print('{0}\t{1}'.format(w1,w2))

if __name__ == "__main__":
    
    main(sys.argv[1:])



