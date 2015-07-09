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
master_dictionary_files_path = "/home/wh/Documents/data/train/total/"
ham_train_files_path = "/home/wh/Documents/data/train/ham/"
spam_train_files_path = "/home/wh/Documents/data/train/spam/"
ham_test_files_path = "/home/wh/Documents/data/test/ham/"
spam_test_files_path = "/home/wh/Documents/data/test/spam/"
test_file_path = "/home/wh/Documents/data/test/spam/5638.2005-07-21.SA_and_HP.spam.txt"
output_ham_file_path = "/home/wh/Documents/data/ham_dictionary"
output_spam_file_path = "/home/wh/Documents/data/spam_dictionary"
    
file_number_path = "file_number.data"

if __name__ == '__main__':
    d = dictionary()
    nb = naivebayes()
    
    d.generate_master_dictionary(master_dictionary_files_path) 
    #print "and occur times : " + str(d.master_dictionary["and"])
    d.filter_master_dictionary()

    spam_dictionary = d.generate_part_master_dictionary(spam_train_files_path, d.master_dictionary)
    ham_dictionary = d.generate_part_master_dictionary(ham_train_files_path, d.master_dictionary)   
    number = [9034,3372,12406]
    
    d.output_dictionary(ham_dictionary, output_ham_file_path)
    d.output_dictionary(spam_dictionary, output_spam_file_path)
    #file_dictionary = d.generate_file_dictionary(test_file_path)        
    #nb.predict(test_file_path, file_dictionary, number, ham_dictionary, spam_dictionary)
    
    #nb.count(ham_test_files_path, number, ham_dictionary, spam_dictionary)
    nb.count(d, ham_test_files_path, number, ham_dictionary, spam_dictionary)
    #nb.count(d, spam_test_files_path, number, ham_dictionary, spam_dictionary)
    
    
    
    
    
    
    