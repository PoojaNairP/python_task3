
class Book:

    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id=book_id

    def display_book_details(self):
        return (f"Book Details\nBook Id: {self.book_id}\n"
              f"Book Title: {self.title}\nBook Author: {self.author}")


class Library:

    def __init__(self):
        self.book_dict={}

    def add(self,book):
        print("Book Added Successfully")
        self.book_dict[book.book_id]=book

    def remove(self,book_id):
        if book_id not in self.book_dict:
            raise ValueError("Book not found")
        del self.book_dict[book_id]
        print("Removed the book successfully")


    def search(self,title):
        found_books = [book.display_book_details() for book in self.book_dict.values() if
                       title.lower() == book.title.lower() or title.lower() in list(book.title.lower().split(" "))]
        #print(found_books)
        if not found_books:
            print("No books found with the given title.")
        else:
            print("Successfully fetched")
            print("\n".join(found_books))


    def __iter__(self):
        for books in self.book_dict.values():
            yield books



class User:

    def __init__(self,userid,name):
        self.userid=userid
        self.name=name


    def display_user_details(self):
        print(f"User Details\nUser Id: {self.userid}"
              f"\nUser Name: {self.name}")

class LibraryUser(User):

    book_list=[]
    def __init__(self, userid, name,library):
        super().__init__(userid, name)
        self.library=library
        self.borrowed_book=[]


    def borrow(self,book_id):
        try:
            if book_id not in self.library.book_dict:
                raise ValueError("Book not found")
            elif book_id in self.book_list:
                raise ValueError("Book has already been borrowed")
            self.borrowed_book.append(book_id)
            self.book_list.append(book_id)
            print("Successfully borrowed the book")
        except ValueError as e:
            print(e)


    def return_book(self,book_id):
        try:
            if book_id not in self.borrowed_book:
                raise ValueError("User hasn't borrowed the book")
            elif book_id not in self.library.book_dict:
                raise ValueError("Book is not present")
            self.borrowed_book.remove(book_id)
            self.book_list.remove(book_id)
            print("Successfully returned the book")
        except ValueError as e:
            print(e)


    def track_books_borrowed(self):
        if self.borrowed_book:
            for book_id in self.borrowed_book:
                print(self.library.book_dict[book_id].display_book_details())
        else:
            print("User hasn't borrowed any book")











