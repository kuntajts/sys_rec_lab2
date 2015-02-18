__author__ = 'andrew'
from collections import defaultdict

class InvertedIndexModel:

    # new basic dictionary
    #invertedIndex = defaultdict(defaultdict())

    def __init__(self, docID):
        self.invertedIndex = defaultdict(lambda : defaultdict())
        self.docID = docID
        self.populateInvertedIndex()


    def populateInvertedIndex(self):
        tokenList = self.getTokensFromCleanFile()

    def getTokensFromCleanFile(self):
        fileName = self.getFileName()
        fo = open(("data/clean/" + fileName), "r")

        term = fo.readline()
        i = 0
        for term in fo:
            if term not in self.invertedIndex:
                self.invertedIndex[term] = defaultdict(list)
            if self.docID not in self.invertedIndex[term]:
                self.invertedIndex[term][self.docID].append(i)
            i = i+1

        fo.close()

    def getFileName(self):
        filename = str(self.docID)
        nameLength = len(filename)
        for i in range(abs(nameLength - 7)):
            filename = "0" + filename

        return filename + ".txt"

