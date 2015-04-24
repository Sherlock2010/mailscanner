'''
Created on Apr 20, 2015

@author: wh
'''
from __future__ import division
import nltk
import os
import math
from common.filesystem.writer.dictionary import dictionary

class naivebayes(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #prior probability when word is not found in it's dictionary 
        self.NOT_EXIT_PROBABILITY = 0.001
        
    def file_number(self, file_number_path):
        f = open("file_number.data", 'r')
        lines = f.readlines()
        number = [int(lines[0]), int(lines[1]), int(lines[2])]
        f.close()
        return number
    
    def calculate_probability(self, file_dictionary, master_dictionary, file_number, total_file_number):
        """
        to calculate the probability of P(x|w) with log function
        """
        result = 0.0
        for (key, value) in file_dictionary.items():
            if(key in master_dictionary):
                #print key
                #print key + " " + str(master_dictionary[key])
                result += math.log(master_dictionary[key]+1) - math.log(file_number)
            else:
                result += math.log(file_number * self.NOT_EXIT_PROBABILITY)
            
        result += math.log(file_number) - math.log(total_file_number)
        #print "-----------"
        return result
    
    
    def predict(self, file_path, file_dictionary, number, ham_dictionary, spam_dictionary):
        """
        predict which kind this file belongs to
        
        @param number: train ham/spam/total files number
        """
        ham_file_number = number[0]
        spam_file_number = number[1]
        total_file_number = number[2]
    
        #print file_dictionary
        ham_probability = self.calculate_probability(file_dictionary, ham_dictionary, ham_file_number, total_file_number)
        spam_probability = self.calculate_probability(file_dictionary, spam_dictionary, spam_file_number, total_file_number)
        
        #print "ham_probability : %f " % ham_probability
        #print "spam_probability : %f " % spam_probability
        if ham_probability > spam_probability :
            return 1
        else :
            return 0
        
    def count(self, d, files_path, number, ham_dictionary, spam_dictionary):
        """
        count the PRECISION by naive bayes
        
        @param number: ham/spam/total files number
        """
        TOTAL_NUMBER = 0
        SPAM_NUMBER = 0
        HAM_NUMBER = 0
        
        #d = dictionary()
    
        files = os.listdir(files_path)
    
        for file in files:
            file_path = files_path + file
        
            file_dictionary = d.generate_file_dictionary(file_path)
            result = self.predict(file_path, file_dictionary, number, ham_dictionary, spam_dictionary)
    
            TOTAL_NUMBER += 1
            
            if(result):
                HAM_NUMBER += 1
            else:
                SPAM_NUMBER += 1
    
        print "TOTAL NUMBER: %d " % TOTAL_NUMBER
        print "HAM NUMBER : %d" % HAM_NUMBER
        print "SPAM NUMBER : %d" % SPAM_NUMBER
        print "PRECISION : %f" % (HAM_NUMBER / TOTAL_NUMBER) 
        
if __name__ == "__main__":
    pass
        
        
        
        