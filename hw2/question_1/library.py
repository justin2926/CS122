from question_1.utils import *

@log_operation
def add_book(library, title, author):
    library.append({'title': title, 'author': author})

@log_operation
def remove_book(library, title):
    for book in library:
        if book.get('title') == title:
            library.remove(book)
        else:
            print(f"Error: Book '{title}' not found.")
            break

def list_books(library):
    if len(library) == 0:
        print("The library is empty.")
    else:
        for book in library:
            print(book)


