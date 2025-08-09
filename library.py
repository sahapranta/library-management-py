class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    def get_book_id(self):
        return self.__book_id

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            return True
        return False

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            return True
        return False

    def is_available(self):
        return self.__availability

    def view_book_info(self):
        status = "Available" if self.__availability else "Not Available"
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Status: {status}")


class Library:
    book_list = []
    
    def entry_book(self, title, author, availability):
        book_id = len(self.book_list) + 1
        book = Book(book_id, title, author, availability)
        self.book_list.append(book)

    def view_all_books(self):
        if not Library.book_list:
            print("No books in the library")
        else:
            for book in Library.book_list:
                book.view_book_info()

    def borrow_book(self, book_id):
        for book in Library.book_list:
            if book.get_book_id() == book_id:
                if book.borrow_book():
                    print("Book borrowed successfully")
                else:
                    print("Book is already borrowed")
                return
        print("Invalid book ID")

    def return_book(self, book_id):
        for book in Library.book_list:
            if book.get_book_id() == book_id:
                if book.return_book():
                    print("Book returned successfully")
                else:
                    print("Book is not borrowed")
                return
        print("Invalid book ID")


library = Library()

library.entry_book("The Alchemist", "Paulo Coelho", True)
library.entry_book("The Da Vinci Code", "Dan Brown", True)
library.entry_book("The Catcher in the Rye", "J.D. Salinger", True)
library.entry_book("The Great Gatsby", "F. Scott Fitzgerald", True)
library.entry_book("The Hobbit", "J.R.R. Tolkien", True)


while True:
    print("\nWelcome to PY Library")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            library.view_all_books()
        elif choice == 2:
            book_id = int(input("Enter book ID: "))
            library.borrow_book(book_id)
        elif choice == 3:
            book_id = int(input("Enter book ID: "))
            library.return_book(book_id)
        elif choice == 4:
            print("Thank you!")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")