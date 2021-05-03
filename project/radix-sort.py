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
    

def main():
    book = radix_a_book()
    for w in book:
        print(w)
        
        
        
if __name__ == '__main__':
    main()
