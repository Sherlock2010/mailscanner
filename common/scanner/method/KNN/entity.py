'''
Created on Aug 4, 2015

@author: wh
'''
from __future__ import division
from numpy import *  
import matplotlib.pyplot as plt  
import time  
import os
from common.filesystem.writer.dictionary import dictionary

f = open("/tmp/out", "w")

class KNN(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.k = 5
        self.dataMat = []
        
        #keep MAX number words that are most frequenct useful for each file 
        self.MAX = 15
        
    def generate_mat(self, d, files_path, label):

        files = os.listdir(files_path)
        
        for file in files:
            dataMatTmp = []

            file_path = files_path + file

            file_dictionary = d.generate_file_dictionary(file_path)

            dataMatTmp.append(file_dictionary)
            dataMatTmp.append(label)
            dataMatTmp.append(file_path)

            self.dataMat.append(dataMatTmp)
           
            
    
    def distance(self, X, Y):
        # X : dictionary
        # Y : dictionary
        XTmp = dict(X)
        YTmp = dict(Y)

        dist = 0
    
        for (key, value) in XTmp.items():
            if(key in YTmp):
                dist += math.pow((XTmp[key]-YTmp[key]), 2)
                YTmp.pop(key)

            else:
                dist += math.pow(XTmp[key], 2)
      
        for (key, value) in YTmp.items():
            dist += math.pow(YTmp[key], 2)

        dist = math.sqrt(dist)

        return dist

    def predict(self, data):
      
        result = 0
        labelList = []
        indexList = []
        dataMatTmp = list(self.dataMat)

        for i in range(self.k):
            dist = self.distance(data, dataMatTmp[0][0])
            index = 0
    
            # search for the closest sample
            for j in range(len(dataMatTmp)):

                dataTmp = dataMatTmp[j]
            
                #dataTmp = [file_dictionary, label, file_path]
                if self.distance(data, dataTmp[0]) < dist:
                    dist = self.distance(data, dataTmp[0])
                    index = j
            
            labelList.append(dataMatTmp[index][1])
            dataMatTmp.remove(dataMatTmp[index])
            indexList.append(index)
    
        for i in range(self.k):
            result += labelList[i]
    
        if (result / self.k) > 0.5:
            # print>>f, "ham mail"
            # print>>f, "\n"
            return 1
        else:
            # print>>f, "spam mail"
            # print>>f, "\n"
            return 0

    def test(self, d, test_ham_files_path, test_spam_files_path):
        #ham mail
        ham_files = os.listdir(test_ham_files_path)

        number = 0
        ham_number = 0

        for file in ham_files:
            file_path = test_ham_files_path + file
            number += 1


            test_file_dictionary = d.generate_file_dictionary(file_path)

            if(self.predict(test_file_dictionary) == 1):
                ham_number += 1
  
        print "ham mail prediction : %f" % (ham_number / number)

        # spam mail
        spam_files = os.listdir(test_spam_files_path)

        number = 0
        spam_number = 0

        for file in spam_files:
            file_path = test_spam_files_path + file
            number += 1

            test_file_dictionary = d.generate_file_dictionary(file_path)
            if(self.predict(test_file_dictionary) == 0):
                spam_number += 1

        print "spam mail prediction : %f" % (spam_number / number)

if __name__ == '__main__':
    #file path
    ham_train_files_path = "/home/wh/Documents/data2/train/ham/"
    spam_train_files_path = "/home/wh/Documents/data2/train/spam/"

    ham_test_files_path = "/home/wh/Documents/data2/test/ham/"
    spam_test_files_path = "/home/wh/Documents/data2/test/spam/"

    ham_test_file_path = "/home/wh/Documents/data2/test/ham/0087.2000-01-05.kaminski.ham.txt"
    spam_test_file_path = "/home/wh/Documents/data2/test/spam/2701.2005-06-27.SA_and_HP.spam.txt"
    master_dictionary_files_path = "/home/wh/Documents/data/train/total/"

    d = dictionary()
    kNN = KNN()
    ham_label = 1
    spam_label = 0

    #generate file dictionary
    d.generate_master_dictionary(master_dictionary_files_path) 
    d.filter_master_dictionary()

    #generate dataMat
    kNN.generate_mat(d, ham_train_files_path, ham_label)
    kNN.generate_mat(d, spam_train_files_path, spam_label)

    # test_file_dictionary = d.generate_file_dictionary(ham_test_file_path)
    # kNN.predict(test_file_dictionary)

    kNN.test(d, ham_test_files_path, spam_test_files_path)

    

        