import re
import sys

from PartA import tokens

# Runtime Complexity: O(n)
if __name__ == '__main__':    
    file1 = open(sys.argv[1], 'r') # O(1)
    tokens1 = tokens(file1) # O(1)
    file2 = open(sys.argv[2], 'r')  # O(1)
    tokens2 = tokens(file2) # O(1)
    file1.close() # O(1)
    file2.close() # O(1)
    file1_set = set(tokens1) # O(n)
    file2_set = set(tokens2) # O(n)

# Find words in common by printing the length of the intersection of both sets    
print(len(file1_set.intersection(file2_set)), end = "")