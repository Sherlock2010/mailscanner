'''
Created on Apr 20, 2015

@author: wh
'''
import nltk
import os


class dictionary(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.master_dictionary = dict()
        self.filter_dictionary = dict()
        
        self.spam_dictionary = dict()
        self.ham_dictionary = dict()
        self.number = []
        
        self.MIN_NUMBER = 1
        self.MAX_NUMBER = 3000
        
    
    def generate_file_dictionary(self, file_path):
        """
        read file to generate consistency dictionary , each word 
        """
        tokenizer = nltk.RegexpTokenizer("[\w']{2,}")   #leave the word with length > 1
        dictionary = dict()
        
        
        
        f = open(file_path, 'r')
        for line in f:
            words = tokenizer.tokenize(line)
            #print words
            for word in words:
                if word in self.master_dictionary:
                    if(word in dictionary):
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1
        f.close()
        
        return dictionary  
    
    def generate_part_master_dictionary(self, files_path, master_dictionary):
        """
        generate ham/spam master dictionary, drop the word not in the filtered master_dictionary
        """
        files = os.listdir(files_path)
        part_master_dictionary = dict()
        """
        for(key, value) in self.master_dictionary.items():
            part_master_dictionary[key] = 0
        """
        for file in files:
            #generate each file dictionary
            
            tokenizer = nltk.RegexpTokenizer("[\w']{2,}")   #leave the word with length > 1
            
            file_dictionary = dict()
            
            f = open(files_path + file, 'r')
            for line in f:
                words = tokenizer.tokenize(line)

                for word in words:
                    if(word not in file_dictionary):
                        file_dictionary[word] = 1
            f.close()
            
            
            for (key, value) in file_dictionary.items():        
                #update value in part_master_dictionary
                #if key is in master_dictionary, then put it into ham/spam dictionary
                if(key in self.master_dictionary):
                
                    if(key in part_master_dictionary):
                        part_master_dictionary[key] += file_dictionary[key]
              
                    else:
                        part_master_dictionary[key] = 1
        
        return part_master_dictionary
        
        
    def generate_master_dictionary(self, files_path):
        """
        merge each file dictionary into master dictionary 
        
        @param files_path: mails parent catalog path
        """
        # list files in files_path
        files = os.listdir(files_path)
        #master_dictionary = dict()
        
        for file in files:
            #generate each file dictionary

            tokenizer = nltk.RegexpTokenizer("[\w']{2,}")   #leave the word with length > 1
            
            file_dictionary = dict()
            
            f = open(files_path + file, 'r')
            for line in f:
                words = tokenizer.tokenize(line)

                for word in words:
                    if(word not in file_dictionary):
                        file_dictionary[word] = 1
            f.close()
            
            
            for (key, value) in file_dictionary.items():        
                #update value in master_dictionary
                if(key in self.master_dictionary):
                    self.master_dictionary[key] += file_dictionary[key]
              
                else:
                    self.master_dictionary[key] = 1
        
        return self.master_dictionary
    
    def file_number(self):
        return self.number
    
    def filter_master_dictionary(self):
        """
        filter the dictionary , leave the words with occur times between MIN_NUMBER and MAX_NUMBER
        """
        
        master_dictionary  = dict()
        
        for (key, value) in self.master_dictionary.items():
            if self.MIN_NUMBER < value and value < self.MAX_NUMBER : 
                master_dictionary[key] = value
            else:
                self.filter_dictionary[key] = value
         
        self.master_dictionary = master_dictionary
                   
                 
    def output_dictionary(self, dictionary, file_path):
        """
        output dictionary to file
        """
        f = open(file_path, 'a+')
        
        for (key, value) in dictionary.items():
            if (value != 0) :
                f.writelines(key+" "+str(value)+"\n")
            
        f.close()
        
if __name__ == "__main__":
    input_file_path = "/tmp/test_data/4252.2001-11-26.kitchen.ham.txt"
    output_file_path = "/tmp/test_data/dictionary.txt"
    master_dictionary_files_path = "/tmp/data/train/total/"
    output_ham_file_path = "/tmp/mail/ham_dictionary"
    output_spam_file_path = "/tmp/mail/spam_dictionary"
    
    d = dictionary()
    
    d.generate_master_dictionary(master_dictionary_files_path) 
    #print "more occur number %d" % d.master_dictionary['more']
    print len(d.master_dictionary)
    #print d.master_dictionary["more"]
    
    d.filter_master_dictionary()
    print len(d.master_dictionary)
       
    file_dictionary = d.generate_file_dictionary(input_file_path)
    d.output_dictionary(file_dictionary, output_file_path)
    
    #master_dictionary = d.generate_master_dictionary(input_files_path)  
    #d.output_dictionary(master_dictionary, output_file_path)  
    
            






