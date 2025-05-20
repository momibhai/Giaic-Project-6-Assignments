class Book:
    total_books = 0

    def __init__(self, name):
        self.name = name
        Book.total_books +=1
        
    @classmethod
    def increment_book_count(cls):
        print(f"A New Book is Added, Total : {cls.total_books}")

b1 = Book("AL Adam")
b1 = Book("AL Adam")
b1 = Book("AL Adam")
b1.increment_book_count()
