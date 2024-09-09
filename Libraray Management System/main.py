from library_module import Library,LibraryUser,Book

library=Library()
users=[]
print("1 : Add book\n"
      "2 : Remove book\n"
      "3 : Search by title\n"
      "4 : Display all book\n"
      "5 : Add User\n"
      "6 : Borrow Book\n"
      "7 : Track Borrowed book\n"
      "8 : Return Borrowed book\n"
      "9 : Quit\n")

while True:
    choice=input("Enter the choice: ")

    if choice=="1":
        while True:
            try:
                book_id=int(input("Enter the book id : "))
                if book_id<0:
                    raise ValueError("Positive integer value expected")
                if book_id in library.book_dict:
                    raise ValueError("Book id already exists.")
                title=input("Enter the title : ")
                author=input("Enter the author : ")
                book=Book(title,author,book_id)
                library.add(book)
                break
            except ValueError as e:
                print(e)
                print("Try again")

    elif choice=="2":
        while True:
            try:
                book_id=int(input("Enter the id of book to be removed : "))
                if book_id<0:
                    raise ValueError
                library.remove(book_id)
                break
            except ValueError:
                print("Positive Integer Expected\nTry again")


    elif choice=="3":
        title=input("Enter the title to be searched : ")
        library.search(title)

    elif choice=="4":
        for book in library:
            details=book.display_book_details()
            print(details)


    elif choice=="5":
        while True:
            try:
                user_id = int(input("Enter the userid : "))
                if user_id<0:
                    raise ValueError("Positive integer Values expected")
                if any(user_id for user in users if user.userid == user_id):
                    raise ValueError("Userid already exists")
                name=input("Enter the name : ")
                user=LibraryUser(user_id,name,library)
                users.append(user)
                break
            except ValueError as e:
                print(e)
                print("Try again")

    elif choice=="6":
        while True:
            try:
                if not users:
                    print("No user added yet....")
                    break
                book_id=int(input("Enter the id of book to be borrowed : "))
                users[-1].borrow(book_id)
                break
            except ValueError:
                print("Integer Value Expected\nTry Again")

    elif choice=="7":
        if not users:
            print("No user added yet....")
        else:
            users[-1].track_books_borrowed()

    elif choice=="8":
        while True:
            try:
                if not users:
                    print("No user added yet....")
                    break
                book_id=int(input("Enter the id of book to be returned : "))
                users[-1].return_book(book_id)
                break
            except ValueError:
                print("Integer Value Expected\nTry Again")


    elif choice=="9":
        break

    else:
        print("Invalid choice...\nTry Again")




# book id unique
# book_id=6
# if any (book_id == bookId["book_id"] for bookId in book.book_list):
#     print("Book id already exists")
# else:
#     print("Doesn't exist")



# print(book.book_list)
#
# print("Removing book in book list")
#
# print(book.book_list)
# print("Removing book not in book list")


#print("\nSearching....")

# print("\nGenerator")


# user=LibraryUser(100,"A")
# user.display_user_details()
#
# print("\nBorrowing")
# user.borrow(2)
# print("Printing user_dict after borrowing first book")
# print(user.user_dict)
# user.borrow(7)
# print("Printing user_dict after borrowing non-existent second book")
# print(user.user_dict)
#
# print("\n\nAdding another user")
# user2=LibraryUser(101,"B")
# user2.display_user_details()
#
# print("\nBorrowing")
# user2.borrow(2)
# print("Printing user_dict after borrowing first book")
# print(user2.user_dict)
# user2.borrow(3)
# print("Printing user_dict after borrowing second book")
# print(user2.user_dict)
#
# print("\nReturning")
# user2.return_book(3)
# print("Printing user_dict after returning second book")
# print(user2.user_dict)
# user2.return_book(4)
#
# print("\nTrack Borrowed books")
# print("\n\nUser1")
# user.track_books_borrowed()
# print("\n\nUser2")
# user2.track_books_borrowed()
#
# print("End")