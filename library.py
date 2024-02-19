# create class
class Library:

    # create constructor method
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, "a+")
            self.file.seek(0)
            print(f"{self.filename} opened.")
        except FileNotFoundError:
            print(f"{self.filename} is not found.")

    # create destructor method
    def __del__(self):
        try:
            self.file.close()
            print(f"{self.filename} closed.")
        except AttributeError:
            pass

    # a. List Books
    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if books:
            print("-" * 15 + "BOOKS" + "-" * 15)
            for index, book in enumerate(books):
                print(f"{index+1}: {book.strip()}")
        else:
            print("There is no book.")

    # b. Add Books
    def add_book(self):
        print("-" * 15 + "ENTER" + "-" * 15)
        title = input("Title: ").strip()
        author = input("Author: ").strip()

        new_book = f"{title} ({author}) \n"
        self.file.writelines(new_book)
        print(f"{title} ({author}) added.")

    # c. Remove Book
    def remove_book(self):
        remove = input("Enter the title: ").strip()
        self.file.seek(0)
        books = self.file.readlines()

        removed_books = [book for book in books if remove not in book]

        if len(removed_books) < len(books):
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(removed_books)
            print(f"{remove} removed.")
        else:
            print(f"There is no book to remove.")


if __name__ == "__main__":

    # create an object
    lib = Library("books.txt")

    while True:
        choice = input("***MENU***\n"
                       "1) List Books\n"
                       "2) Add Book\n"
                       "3) Remove Book\n"
                       "Press q to exit.\n"
                       "Enter the action: ").strip()

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "q" or choice == "Q":
            quit()
        else:
            print("Invalid choice. Try again!")


