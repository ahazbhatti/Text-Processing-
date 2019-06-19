import re
import sys
'''
Created on Apr 10, 2019
@author: Ahaz
'''
# Runtime complexity: O(n^2)
def tokens(file):
    #This is the dictionary where I store the freq counts
    dict = {}
    #I use regex to verify proper alphanumeric input
    regex = re.compile('[^a-zA-Z0-9]')
    # Iterate through the open file object
    for line in file:
    #non alphabets replaced with white space
        myline = regex.sub(' ',line).lower()
    #Words in the string, add it to dict
        for myword in myline.strip().split():
            if myword not in dict:
                dict[myword] = 0
            dict[myword] = dict[myword]+1
    
    return dict

if __name__ == '__main__':

    file = open(sys.argv[1])  #complexity: O(1)
    dict = tokens(file)
    # Create a new list ordered by values in the key
    dict = sorted(sorted(dict.items()),key=lambda kv : kv[1],reverse=True)
     
    if len(dict) != 0: #Complexity O(1)
        print(dict[0][0] + "\t" + str(dict[0][1]), end = "")
    if len(dict) >= 1:  #Complexity O(1)
        for key in dict:
            print("\n" + key[0] + "\t" + str(key[1]), end = "")