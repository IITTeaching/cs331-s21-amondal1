"""""""""""""""""""""
from test.support import temp_cwd
from chardet.enums import CharacterCategory
Name: Abheek Mondal
Class: CS 331
Teacher: Boris Glavic
TA: Christopher Sherman

"""""""""""""""""""""
"""""""""""""""""""""

###Thought Process###
Given an array of unsorted words:
Convert to bits
Sort bits using radix sort
Decode said words
Display the words

All the code written in this project have been written by me, after I thouroughly understood what each line does, I also looked at a lot of sources, couple of the main ones are listed below:
- https://www.geeksforgeeks.org/radix-sort/#:~:text=We%20can%27t%20use%20counting,than%20comparison-based%20sorting%20algorithms.&text=Radix%20sort%20uses%20counting%20sort,to%20the%20most%20significant%20digit.
- https://www.geeksforgeeks.org/python-program-for-counting-sort/
- Wikipedia entry: https://en.wikipedia.org/wiki/Radix_sort
- Youtube video explaining radix sort: https://www.youtube.com/watch?v=6YyflHO9GdE
- Youtube lecture, jump to around min 40: https://www.youtube.com/watch?v=Nz1KZXbghj8
- https://www.codingeek.com/algorithms/radix-sort-explanation-pseudocode-and-implementation/
- http://www.asciitable.com
- and more...


"""""""""""""""""""""

import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

#def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'): #This is not needed
 #   return radix_sort(book_to_words())                              #take in the book and return words sorted
    
def radix_sort(lst):
    if len(lst) == 0:
        return lst
    
    for i in range(len(lst)): #to make sure all words are the same length
       lst[i] = lst[i].ljust(longest(lst))
    
    max = longest(lst)
    char = 0                                                         #keep track of position
    while char != max:                                      # char is smaller than the max number
        while True:                                                 #keep looping, I ran into error where it would occasionally stop for no reason
            count =0                                                 
            for i in range(len(lst)-1):                              #go through list      
                pointer = charbit(lst,i,char)                                #take HTML ASCII value for comparison
                nextword = charbit(lst,i+1,char)                              
                prepointer = charbit(lst,i,char-1)                         
                prenextword = charbit(lst,i+1,char-1)                       
                if prepointer == prenextword:                                  #if the two words have same previous character, check if we should swap them
                      if pointer > nextword:                                 #comparing next character since the previous character is the same
                          lst[i], lst[i+1] = lst[i+1], lst[i]            #swap
                          count+=1                                 
            #print(lst) 
            if count == 0:                                           #Everything is sorted
               break 
                                             
        char+=1     
    words = []                                                      
    for i in range(len(lst)):                                       
         words.append(lst[i].decode('ascii'))                        
    return words                                                  

def charbit(lst, i, char):                                       #this is to obtain the ascii value for the character                                                                   
        value = lst[i][char]       #get the ascii code from book_to_words                                 #
        if value < 64 and value > 123: #A-z as per the ASCII table                              
            temp =  value / 59 #123-64 to give them a position from   0-59 for easier comparisons                                   
            return temp         
        else:                                                       
            return value                                               
                                        
#def swap (lst,x,y):                                       #This one didnt work so it was killed off
#    lst[x],lst[y] = lst[y], lst[x]
#    return lst

def longest(lst):                               #Find longest word length
    max = -float('inf')         # lower bound is -infinity so anything is bigger
    for i in lst:               #go through the list
        if len(i)>max:          #if a bigger word length is found, set it as max
            max = len(i)
    #print(max)
    return max                                            

def main():
    templst = book_to_words()[:100]         
    #print(templst)                     
    print(radix_sort(templst))                                      
                                              
if __name__ == '__main__':
    main()    