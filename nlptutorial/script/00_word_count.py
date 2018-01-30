# -*- coding: utf-8 -*-
"""

Word Count
"""

# import
import sys


fh = open(sys.argv[1], 'r', encoding='utf-8')

# creating an ampthy dictionary
word_count=dict()

for line in fh:
    words = line.lower().split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
#print(word_count)
n = len(word_count.keys())
print("No of unique words: ",n)
print("First few word frequency:" )

if n > 10:
    print({k :  word_count[k] for k in list(word_count)[:10]})    
else:
    print({k :  word_count[k] for k in list(word_count)[:n]})    

# close the file handler
fh.close()

