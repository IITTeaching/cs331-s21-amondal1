import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    pass
#def radix_a_book(book-url='https://www.gutenberg.org/files/84/84-0.txt'):
lst = ['apple', 'cat', 'apple', 'doge', 'rat', 'fish', 'xylophone', 'grass']
print(radixSort(lst))


def radixSort(array):
    maxLen = -1
    for string in array: # Find longest string
        strLen = len(string)
        if strLen > maxLen:
            maxLen = strLen
    oa = ord('a') - 1; # First character code
    oz = ord('z') - 1; # Last character code
    n = oz - oa + 2; # Number of buckets (+empty character)
    buckets = [[] for i in range(0, n)] # The buckets
    for position in reversed(range(0, maxLen)):
        for string in array:
            index = 0 # Assume "empty" character
            if position < len(string): # Might be within length
                index = ord(string[position]) - oa
            buckets[index].append(string) # Add to bucket
        del array[:]
        for bucket in buckets: # Reassemble array in new order
            array.extend(bucket)
            del bucket[:]
    return array

def chartoASCII(array):

    pass
#def radix_a_book(book-url='https://www.gutenberg.org/files/84/84-0.txt'):
lst = ['apple', 'cat', 'apple', 'doge', 'rat', 'fish', 'xylophone', 'grass']
print(radixSort(lst))


#    pass
