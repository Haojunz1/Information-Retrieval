# python cmsc476_p1.py /Users/haojunzhu/desktop/p1_files /Users/haojunzhu/desktop/tokenFiles

import os
import re
import sys
import nltk
from nltk.book import *

#path_input = "/Users/haojunzhu/desktop/test_files" 


################################################################
# remove html tags
pat_html = re.compile(r'<[^>]+>',re.S) 

# Regular expression filters special symbols with spaces, 
# double quotes, single quotes, periods, commas
pat_letter = re.compile(r'[^a-zA-Z \']+')

# Common abbreviations
pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
pat_s = re.compile("(?<=[a-zA-Z])\'s") # Find the letter after the letter
pat_s2 = re.compile("(?<=s)\'s?")
pat_not = re.compile("(?<=[a-zA-Z])n\'t") # not
pat_would = re.compile("(?<=[a-zA-Z])\'d") # would
pat_will = re.compile("(?<=[a-zA-Z])\'ll") # will
pat_am = re.compile("(?<=[I|i])\'m") # am
pat_are = re.compile("(?<=[a-zA-Z])\'re") # are
pat_ve = re.compile("(?<=[a-zA-Z])\'ve") # have

##################################################################
def main():
     
     # receive input and output file path from command line
     path_input = sys.argv[1]
     path_output = sys.argv[2]
     
     # loop files through the directory
     directory = os.listdir(path_input) 
     pad_string = [] # list to store padded string
     
     for file in directory: 

          if not os.path.isdir(file): 

               f = open(path_input+"/"+file, errors="ignore")
               
               iter_file = iter(f)
               
               string = ""
               
               for line in iter_file: 
                    string = string + line   
                    
               string = pat_html.sub('',string)
               string = pat_is.sub(r"\1 is", string)
               string = pat_s.sub("", string)
               string = pat_s2.sub("", string)
               string = pat_not.sub(" not", string)
               string = pat_would.sub(" would", string)
               string = pat_will.sub(" will", string)
               string = pat_am.sub(" am", string)
               string = pat_are.sub(" are", string)
               string = pat_ve.sub(" have", string)
               string = string.replace('\'', ' ')
               string = pat_letter.sub(' ', string).strip().lower()
                    
               pad_string.append(string)
               # tokenPath = "/Users/haojunzhu/desktop/tokenFiles"

               tokenPath = path_output

               # write the tokenized content to the file               
               fToken = open(tokenPath+"/"+file, 'w')
               fToken.write(str(nltk.word_tokenize(string)))
               fToken.close()              
               # print(string)
     
     # store all of the words in a dictionary and count the frequency
     dic = {}
     for text in pad_string:
          text1 = nltk.word_tokenize(text)
          #print(text1)

          for word in text1:
               if word not in dic:
                    dic[word] = 1
               else:
                    dic[word] += 1

     # sort by the freqency and alphabet
     FreqResult= sorted(dic.items(),key=lambda x:x[1],reverse =True)
     AphResult= sorted(dic.items())

     # store to the txt file
     fw1 = open('FreqResult.txt','w')
     for pair in FreqResult:
          fw1.write(str(pair))
          fw1.write('\n')
     fw1.close()

     fw2 = open('AphResult.txt','w')
     for pair in AphResult:
          fw2.write(str(pair))
          fw2.write('\n')
     fw2.close()

main()
