import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    request = urllib.request.urlopen(book_url).request().decode()[1:]
    strng = padding(text.split())
    return strng 
    
def radix_sort(s,swap,longest):
    max = longest(s)
    for x in range (max-1,0,-1):
        for val in range(len(s)):
            for e in range(val,len(s)):
                try:
                    if (s[val][x]>s[val+1][x]):
                        swap(s[val],s[val+1])
                except:
                    pass
    return s

def swap (s,x,y):
    s[x],s[y] = s[y], s[x]
    return s
    
def longest(s):
    max = 0
    for i in s:
        if(len(s)>max):
            max = len(s)
    return max
    

def main():
    s = book_to_words()
    print(s[0:10])
    print("test")
    
    
   #book = radix_a_book()
        
        
if __name__ == '__main__':
    main()
