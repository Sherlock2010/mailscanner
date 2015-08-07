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
        self.k = 0

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
        
        tmp = 0
        tmp1 = 0
        tmp2 = 0
        tmp3 = 0
        """
        for (key, value) in XTmp.items():
            if(key in YTmp):
                dist += math.pow((XTmp[key]-YTmp[key]), 2)
                YTmp.pop(key)

            else:
                dist += math.pow(XTmp[key], 2)
      
        for (key, value) in YTmp.items():
            dist += math.pow(YTmp[key], 2)

        dist = math.sqrt(dist)
        """

        for (key, value) in XTmp.items():
            if key in YTmp:
                tmp1 += XTmp[key] * YTmp[key]

            tmp2 += math.pow(XTmp[key], 2)

        for (key, value) in YTmp.items():
            tmp3 += math.pow(YTmp[key], 2)

        tmp = math.sqrt(tmp2) + math.sqrt(tmp3) 

        if tmp !=0 :
            dist = tmp1 / tmp
        else:
            dist = 0

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
                if self.distance(data, dataTmp[0]) > dist:
                    dist = self.distance(data, dataTmp[0])
                    index = j
            
            # print dataMatTmp[index][2]
            labelList.append(dataMatTmp[index][1])
            dataMatTmp.remove(dataMatTmp[index])
            indexList.append(index)
    
        for i in range(self.k):
            result += labelList[i]
    
        if (result / self.k) > 0.5:
            # print "ham mail"
            # print>>f, "ham mail"
            # print>>f, "\n"
            return 1
        else:
            # print "spam mail"
            # print>>f, "spam mail"
            # print>>f, "\n"
            return 0

    def draw(self, k_range, ham_predition_list, spam_predition_list):
        """
        draw in figure
        """
        plt.xlabel('K Value')
        plt.ylabel('Predition')
        plt.title('Line Graph of KNN')

        plt.plot(k_range, ham_predition_list, 'og--', label = 'ham_predition_line')
        plt.plot(k_range, spam_predition_list, 'or--', label = 'spam_predition_line')
    
        # set axis limits
        plt.xlim(0.0, 10.0)
        plt.ylim(0.5, 1.0)

        legend = plt.legend(loc='lower center', shadow=True)

        # Put a nicer background color on the legend.
        legend.get_frame().set_facecolor('#00FFCC')

    
        plt.show()

    def test(self, d, test_ham_files_path, test_spam_files_path):
        #ham mail
        ham_files = os.listdir(test_ham_files_path)

        number = 0
        ham_number = 0
        ham_predition = 0

        for file in ham_files:
            file_path = test_ham_files_path + file
            number += 1
            # print file_path

            test_file_dictionary = d.generate_file_dictionary(file_path)

            if(self.predict(test_file_dictionary) == 1):
                ham_number += 1
        
        ham_predition = ham_number / number
        print >>f, "ham mail prediction : %f" % ham_predition

        # spam mail
        spam_files = os.listdir(test_spam_files_path)

        number = 0
        spam_number = 0
        spam_predition = 0

        for file in spam_files:
            file_path = test_spam_files_path + file
            number += 1
            # print file_path

            test_file_dictionary = d.generate_file_dictionary(file_path)
            if(self.predict(test_file_dictionary) == 0):
                spam_number += 1


        spam_predition = spam_number / number

        print >>f, "spam mail prediction : %f" % spam_predition

        return ham_predition, spam_predition

    def test2(self, d, file_path_1, file_path_2):
        file_dictionary_1 = d.generate_file_dictionary(file_path_1)
        file_dictionary_2 = d.generate_file_dictionary(file_path_2)

        return self.distance(file_dictionary_1, file_dictionary_2)


if __name__ == '__main__':

    start_time = time.time()
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

    k_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ham_predition_list = []
    spam_predition_list = []

    #generate file dictionary
    d.generate_master_dictionary(master_dictionary_files_path) 
    d.filter_master_dictionary()
   

    #generate dataMat
    kNN.generate_mat(d, ham_train_files_path, ham_label)
    kNN.generate_mat(d, spam_train_files_path, spam_label)

    # test case 1
    # test_file_dictionary = d.generate_file_dictionary(ham_test_file_path)
    # kNN.predict(test_file_dictionary)


    # test case 2
    for i in k_range:
        kNN.k = i
        ham_predition, spam_predition = kNN.test(d, ham_test_files_path, spam_test_files_path)

        ham_predition_list.append(ham_predition)
        spam_predition_list.append(spam_predition)

    # test case 3
    # file_path_1 = "/home/wh/Documents/data2/test/ham/0087.2000-01-05.kaminski.ham.txt"
    # file_path_2 = "/home/wh/Documents/data2/train/ham/2799.2000-11-08.farmer.ham.txt"
    # file_path_3 = "/home/wh/Documents/data2/train/spam/2781.2004-11-10.GP.spam.txt"
    # print kNN.test2(d, file_path_1, file_path_2)
    # print kNN.test2(d, file_path_1, file_path_3)

    end_time = time.time()
    print "program run for %f seconds" % (end_time - start_time)
    kNN.draw(k_range, ham_predition_list, spam_predition_list)

    

        