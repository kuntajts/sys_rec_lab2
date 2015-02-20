__author__ = 'andrew'

import InvertedIndexModel
import Database
import math
from collections import defaultdict

class BooleanRetrievalController:

    invertedIndex = None
    database      = None

    def __init__(self):
        #set Inverted Index
        self.invertedIndex = InvertedIndexModel.InvertedIndexModel()
        self.database = Database.WebDB("data/cache/database.db")
        return

    def queryIngest(self, queryType):
        if(queryType == "1"):
            self.singleTokenQuery()
        elif(queryType == "2"):
            self.andQuery()
        elif(queryType == "3"):
            self.orQuery()
        elif(queryType == "4"):
            self.phraseQuery()
        elif(queryType == "5"):
            self.nearQuery()

    def singleTokenQuery(self):
        query = input("Please enter a single word: ")
        i = 1
        finalResult = defaultdict(int)
        for key in self.invertedIndex.invertedIndex[query]:
            result = self.database.getInfoByID(key)
            url = result[0][0]
            title = result[0][1]
            type = result[0][2]
            name = self.database.getItemByID(key)

            finalResult[name] += 1
            print(str(i) + ".\t" + title + "\n\t" + url + "\n\t" + type + ": " + name + "\n")
            i += 1

        print("total: " + str(i-1))
        highestValue = 0
        highestKey = ''
        for item in finalResult:
            if finalResult[item] > highestValue:
                highestValue = finalResult[item]
                highestKey = item

        print(highestKey + " ("+str(highestValue)+")")

    def andQuery(self):
        query1 = input("Please enter first word: ")
        query2 = input("Please enter second word: ")
        i = 1
        list1 = self.invertedIndex.invertedIndex[query1]
        list2 = self.invertedIndex.invertedIndex[query2]
        list3 = set(list1) & set(list2)
        finalResult = defaultdict(int)
        for key in list3:
            result = self.database.getInfoByID(key)
            url = result[0][0]
            title = result[0][1]
            type = result[0][2]
            name = self.database.getItemByID(key)

            finalResult[name] += 1
            print(str(i) + ".\t" + title + "\n\t" + url + "\n\t" + type + ": " + name + "\n")
            i += 1
        print("total: " + str(i-1))
        highestValue = 0
        highestKey = ''
        for item in finalResult:
            if finalResult[item] > highestValue:
                highestValue = finalResult[item]
                highestKey = item

        print(highestKey + " ("+str(highestValue)+")")

    def orQuery(self):
        query1 = input("Please enter first word: ")
        query2 = input("Please enter second word: ")
        i = 1
        list1 = self.invertedIndex.invertedIndex[query1]
        list2 = self.invertedIndex.invertedIndex[query2]
        list3 = set(list1) | set(list2)
        finalResult = defaultdict(int)

        for key in list3:
            result = self.database.getInfoByID(key)
            url = result[0][0]
            title = result[0][1]
            type = result[0][2]
            name = self.database.getItemByID(key)

            finalResult[name] += 1
            print(str(i) + ".\t" + title + "\n\t" + url + "\n\t" + type + ": " + name + "\n")
            i += 1

        print("total: " + str(i-1))
        highestValue = 0
        highestKey = ''
        for item in finalResult:
            if finalResult[item] > highestValue:
                highestValue = finalResult[item]
                highestKey = item

        print(highestKey + " ("+str(highestValue)+")")

    def phraseQuery(self):
        query1 = input("Please enter first word: ")
        query2 = input("Please enter second word: ")

        dict1 = self.invertedIndex.invertedIndex[query1]
        dict2 = self.invertedIndex.invertedIndex[query2]
        list3 = list(set(dict1) & set(dict2))
        finalResult = defaultdict(int)
        i = 1
        for item in list3:
            for dict1Elements in dict1[item]:
                for dict2Elements in dict2[item]:
                    if dict1Elements+1 == dict2Elements:
                        result = self.database.getInfoByID(item)
                        url = result[0][0]
                        title = result[0][1]
                        type = result[0][2]
                        name = self.database.getItemByID(item)
                        finalResult[name] += 1
                        print(str(i) + ".\t" + title + "\n\t" + url + "\n\t" + type + ": " + name + "\n")
                        i = i+1

        print("total: " + str(i-1))
        highestValue = 0
        highestKey = ''
        for item in finalResult:
            if finalResult[item] > highestValue:
                highestValue = finalResult[item]
                highestKey = item

        print(highestKey + " ("+str(highestValue)+")")



    def nearQuery(self):
        query1 = input("Please enter first word: ")
        query2 = input("Please enter second word: ")

        dict1 = self.invertedIndex.invertedIndex[query1]
        dict2 = self.invertedIndex.invertedIndex[query2]
        list3 = list(set(dict1) & set(dict2))
        finalResult = defaultdict(int)
        i = 1
        for item in list3:
            for dict1Elements in dict1[item]:
                for dict2Elements in dict2[item]:
                    difference = math.fabs(dict1Elements - dict2Elements)
                    if difference <= 5:
                        result = self.database.getInfoByID(item)
                        url = result[0][0]
                        title = result[0][1]
                        type = result[0][2]
                        name = self.database.getItemByID(item)
                        finalResult[name] += 1
                        print(str(i) + ".\t" + title + "\n\t" + url + "\n\t" + type + ": " + name + "\n")
                        i = i+1

        print("total: " + str(i-1))
        highestValue = 0
        highestKey = ''
        for item in finalResult:
            if finalResult[item] > highestValue:
                highestValue = finalResult[item]
                highestKey = item

        print(highestKey + " ("+str(highestValue)+")")