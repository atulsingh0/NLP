# -*- coding: utf-8 -*-
"""

Word Count
"""

# import
import sys


fh = open(sys.argv[1], 'r')

# creating an ampthy dictionary
word_count=dict()

for line in fh:
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
print(word_count)

# close the file handler
fh.close()

