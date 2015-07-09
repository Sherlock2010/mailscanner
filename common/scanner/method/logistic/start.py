'''
Created on May 9, 2015

@author: wh
'''
from __future__ import division
from common.filesystem.writer.dictionary import dictionary
#import common.filesystem.writer.dictionary as d
from entity import logistic

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
    
if __name__ == '__main__':
    d = dictionary()
    lg = logistic()
    
    d.generate_master_dictionary(master_dictionary_files_path) 
    d.filter_master_dictionary()
    
    lg.generate_matrix(d, ham_train_files_path, spam_train_files_path, d.master_dictionary)
    lg.count()
    
    
    
    
    
    
    