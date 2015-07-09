'''
Created on May 6, 2015

@author: wh
'''

from __future__ import division
from numpy import *  
import matplotlib.pyplot as plt  
import time  
import os
from common.filesystem.writer.dictionary import dictionary


   
class logistic(object):
    '''
    classdocs
    '''

    def __init__(self):
        """
        Constructor
        """
        # represents a mail is ham or spam mail
        self.labelMat = []
        # each row represents a word list in a mail
        self.dataMat = []
        # word index in master dictionary
        self.word_vector = []
        self.indexMat = []
        self.index_dictionary = dict()

    # calculate the sigmoid function  
    def sigmoid(self, inX):  
        return 1.0 / (1 + exp(-inX))
      
      
    #load data from file
    def generate_matrix(self, d, files_path, master_dictionary, label):
        """
        @param d: dictionary instance
        @param files_path: train data's path
        @param master_dictionary: dictionary contains   
        @param label: 1 presents ham mail ; 0 presents spam mail
        
        generate data matric
        each row denotes one sample
        each column denotes one label (word number)
      
        """
        
        #dataMat:
        #      denotes the features in each sample like this: (x1, x2, x3 ...)
        #labelMat:
        #      denotes each sample's lable , like (ham mail or spam mail) 
        i = 0
        dataMat = []
        labelMat = []
        
        files = os.listdir(files_path)
        
        for file in files:
            file_path = files_path + file
            file_dictionary = d.generate_file_dictionary(file_path)
            
            labelMat.append(label)

            dataMatTmp = [] 
            indexMatTmp = []
            
            for (key, value) in file_dictionary.items(): 
                indexMatTmp.append(self.index_dictionary.get(key))    
                dataMatTmp.append(value)  
                  
            
            self.dataMat.append(dataMatTmp)
            self.indexMat.append(indexMatTmp)

        
        return dataMat, labelMat
            
     
    def generate_index_dictionary(self, master_dictionary):
        
        index = 0
        
        for (key, value) in master_dictionary.item():
            self.index_dictionary[key] = index
            index += 1
            
                 
                   
    def gradAscent(self):
        """
        dataMatrix = mat(dataMatIn)
        labelMatrix = mat(classLabels).transpose()
        """
        
        #m denotes the row number
        #n denotes the column number
        m, n = shape(dataMatrix)
        
        alpha = 0.001
        maxCycles = 500
        weights = ones((n, 1))
        
        print shape(dataMatrix)
        print dataMatrix
        
        for k in range(maxCycles):
            """
            h = self.sigmoid(dataMatrix * weights)
            error = (labelMatrix - h)
            weights = weights + alpha * dataMatrix.transpose() * error
            """
            
        return weights
                
    def count(self, dataMatric, labelMatrix): 
        """
        count predict result of ham/spam mails
        """
        row, cloumn = shape(dataMatric)
        
        weights = self.gradAscent(dataMatric, labelMatrix)
        
        ham_number = 0
        ham_correct_number = 0
        ham_error_number = 0
        
        spam_number = 0
        spam_correct_number = 0
        spam_error_number = 0
        
        for r in range(1, row):
            probability = self.sigmoid(self.dataMatric[r] * weights)
            
            if(probability >= 0.5):
                ham_number += 1
                
                if(self.labelMatric[r]):
                    ham_correct_number += 1
                else:
                    ham_error_number += 1
                    
            else:
                spam_number += 1
                
                if(not self.labelMatric[r]):
                    spam_correct_number += 1
                else:
                    spam_error_number += 1
                    
        print "HAM PRECISION : %f" % (ham_correct_number / ham_number)
        print "SPAM PRECISION : %f" % (spam_correct_number / spam_number)  
        
        
        
if __name__ == '__main__':
    master_dictionary_files_path = "/home/wh/Documents/data/train/total/"
    ham_train_files_path = "/home/wh/Documents/data/train/ham/"
    spam_train_files_path = "/home/wh/Documents/data/train/spam/"
    ham_label = 1
    spam_label = 0

    d = dictionary()
    lg = logistic()
    
    d.generate_master_dictionary(master_dictionary_files_path) 
    d.filter_master_dictionary()
    
    dataMatrix, labelMatrix = lg.generate_matrix(d, ham_train_files_path, ham_label)
    #lg.generate_matrix(d, ham_train_files_path, spam_train_files_path, d.master_dictionary)
    
    #lg.gradAscent(dataMatrix, labelMatrix)
    
    
           

        



    
    
    