'''
Created on Apr 20, 2015

@author: wh
'''
from __future__ import division
from common.filesystem.writer.dictionary import dictionary
#import common.filesystem.writer.dictionary as d
from entity import naivebayes
 
#import entity

"""
test naivebayes
"""

train_data = "./hw1_data/train/"
test_data = "./hw1_data/test/"
#file_dictionary_path = "/tmp/mail/mail_dictionary.txt" # pick up one file to test the program
master_dictionary_files_path = "/tmp/data/train/total/"
ham_train_files_path = "/tmp/data/train/ham/"
spam_train_files_path = "/tmp/data/train/spam/"
ham_test_files_path = "/tmp/data/test/ham/"
spam_test_files_path = "/tmp/data/test/spam/"
test_file_path = "/tmp/test_data/2751.2004-11-07.GP.spam.txt"

file_number_path = "file_number.data"

if __name__ == '__main__':
    d = dictionary()
    nb = naivebayes()
    
    d.generate_master_dictionary(master_dictionary_files_path) 
    print "more " + str(d.master_dictionary["more"])
    d.filter_master_dictionary()

    spam_dictionary = d.generate_part_master_dictionary(spam_train_files_path, d.master_dictionary)
    ham_dictionary = d.generate_part_master_dictionary(ham_train_files_path, d.master_dictionary)   
    number = [9034,3372,12406]

    
    file_dictionary = d.generate_file_dictionary(test_file_path)
            
    nb.predict(file_dictionary, number, ham_dictionary, spam_dictionary)
    #nb.count(spam_test_files_path, number, ham_dictionary, spam_dictionary)
    #nb.count(spam_test_files_path, number, ham_dictionary, spam_dictionary)
    
    
    
    
    
    
    