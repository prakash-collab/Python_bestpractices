# This is Liabrary management exercise to practice the OOPS concepts
''' 
Structure
Concepts: Composition, Class Interaction, Lists of Objects
Requirements : 
    Class: Book, Library
    Library stores list of books.

    Methods: add book, remove book, search book by title or author.
'''


from numpy.random import randint
class Book:

    def __init__(self,title,author):
        self.book_id = randint(0,100)
        self.book_title = title
        self.book_author = author
    
    def __del__(self):
        print('The Book is deleted')

class Library:

    def __init__(self):
        self.lst_book = []

    def add_book(self,title,author):
        self.lst_book.append(Book(title,author))

    def remove_book(self,title):
        for book in self.lst_book:
            if(book.book_title == title):
                self.lst_book.remove(book)
                return 'Removed'

    def search_book(self,title):
        for book in self.lst_book:
            if(book.book_title == title):
                print(f'Yes the book is present and author is {book.book_author}, and its id is {book.book_id}')
            

def main():
    count = 1
    while count:
        user_input = int(input('press 1 for making list of books\npress 2 for remove book\npress 3 for search book'))
        if(user_input == 1):
            obj_library = Library()
            title = input('Please Enter book title')
            author = input('Please enter author name')
            obj_library.add_book(title,author)
        
        elif(user_input == 2):
            title = input('Enter book title to remove')
            obj_library.remove_book(title)
        
        elif(user_input == 3):
            title = input('Enter book title to remove')
            obj_library.search_book(title)

        count = int(input('Press 0 to stop the program, else other key'))

if __name__ == '__main__':
    main()