# spell-checker-python
Comparing different data structures in Python in the context of a spell checking program

This program takes an input dictionary and stores it in either a hash table or a binary search tree. Then, the program searches through a specified text file and checks it for spelling errors by comparing against the dictionary.

To use the program, you can use the terminal commands:  
python3 speller_hashset.py -d [dict path] -s [initial size of hash table (the table will rehash)] [text path]  
python3 speller_bstree.py -d [dict path] [text path]
