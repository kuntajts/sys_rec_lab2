__author__ = 'andrew'
import os, os.path
from collections import defaultdict
import pprint

class InvertedIndexModel:

    # new basic dictionary
    def __init__(self):
        self.invertedIndex = defaultdict()
        self.populateInvertedIndex()
        self.printInvertedIndex()


    def populateInvertedIndex(self):
        DIR = 'data/clean'
        length = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

        for x in range(1, length):
            zeroLen = 7 - len(str(x))
            zeroString = ''
            for num in range(0, zeroLen):
                zeroString += "0"
            file = open("data/clean/" + zeroString + str(x) + ".txt")
            i = 0
            for token in file:
                token = token.rstrip('\n')
                if self.invertedIndex.get(token, None) is not None:
                    self.invertedIndex[token][zeroString + str(x)].append(i)
                else:
                    self.invertedIndex[token] = defaultdict(list)
                    self.invertedIndex[token][zeroString + str(x)].append(i)
                i=i+1
            file.close()


    def printInvertedIndex(self):
        print(self.invertedIndex)

