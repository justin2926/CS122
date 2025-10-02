def log_operation(func):
    def wrapper(*args, **kargs):
        print(f"Executing ", func.__name__)
        func(*args, **kargs)
    return wrapper

filter_by_author = lambda lib, auth: list(filter(lambda book: book['author'] == auth, lib))

def book_generator(library):
    for book in library:
        yield book