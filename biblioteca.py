class Book:
    def __init__(self,title:str):
        self.title=title
        self.available=True

    def book_info(self):
        return f"{self.title},{self.available}"


class User:
    def __init__(self,user):
        self.user=user


class Library:
    def __init__(self):
        self.books=[]
        self.users=[]
        self.loans=[]

    def add_book(self,name):
        self.name=name
        self.books.append(name)

    def available_books(self):
        return f"Books available: {self.books}"
    
    def add_user(self,name):
        self.name=name
        self.users.append(name)
    
    def show_users(self):
        return f"Users registered: {self.users}"
    

    def loan_book(self,book,user):
        if book in self.books:
            self.user=user
            self.books.remove(book)
            book.append()

b = Book("Cartea 1")
d=Book("Cartea 2")

i=User("user 1")

biblioteca=Library()

biblioteca.add_book(b)
biblioteca.add_user(i)
print(biblioteca.show_users())
print(biblioteca.available_books())

