class Library():
    def __init__(self, list_of_books, Library_name):
        # creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No author have lend this book
            self.lend_data[books] = None

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def remove_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)

    def lendbook(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = author
            else:
                print("\nbook pehla thi",lend_data[book]," ne aapel che")
        else:
            print("\nbook library maj nthi")

    def return_book(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] == author:
                self.lend_data[book] = None
            else:
                print("\nbook tmne aapeli j nthi")
        else:
            print("\nbook library maj nthi")

    def display_book(self):
        print(self.list_of_books)

if __name__ == "__main__":
    list_books = ['Cookbook', 'Motu Patlu', 'Chacha_chaudhary', 'Rich Dad and Poor Dad']
    Library_name = 'Harry'
    secret_key = 123456

    praful = Library(list_books, Library_name)

    print(f"Welecome To {praful.library_name} library\n\n")
    exit = False

    while(exit is not True):
        print(f"'end' for exit \n"
              f"Display Book Using 'd'\n"
              f"add lend book using 'l'\n"
              f"Return a Book using 'r' \n"
              f"Add Book Using 'add'\n"
              f"Delete Book using 'del' \n "
              f"")
        a = input("Enter your choice")
        if a == "end":
            exit = True
        elif a == "d":
            praful.display_book()
        elif a == "l":
            authorinput = input("Whats your name")
            bookinput = input("which book")
            praful.lendbook(bookinput, authorinput)
            print(praful.lend_data)
        elif a == "r":
            authorinput = input("Whats your name")
            bookinput = input("which book")
            praful.return_book(bookinput, authorinput)
            print(praful.lend_data)
        elif a == "add":
            bookinput = input("book name")
            praful.add_book(bookinput)
        elif a == "del":
            bookinput = input("book name")
            praful.remove_book(bookinput)