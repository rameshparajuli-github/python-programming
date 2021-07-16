class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvaliableBooks(self):
        print("Books Avaliable in this library are: ")
        for book in self.books:
            print(" " + book)
            
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You Have been issued {bookName}. Please keep this book safe and return it within 30 days")
            self.books.remove(bookName)
            return True

        else:
            print("Sorry , This book has already been issude to someone else. Please wait until the book is returned.")
            return False

    def returnBook(self,bookNmae):
        self.books.append(bookNmae)
        print("Thanks for returnig book! Hope you enjoyed reading it. ")


class Student:
    def requestBook(self):
        self.book= input("Enter the name of book you want borrow: ")
        return self.book


    def returnBook(self):
        self.book= input("Enter the name of book you want return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Python", "Django", "Algorithms", "Java", "Flutter"])
    Student = Student()
    # centralLibrary.displayAvaliableBooks()
    while (True):
        welcomeMsg='''********** Welcome To Central Library **********
        Please choose an option:
        1. List all the books
        2. Request a book 
        3. Add/Return a book 
        4. Exit the library
         '''
        print(welcomeMsg)
        
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvaliableBooks()

        
        elif a == 2:
            centralLibrary.borrowBook(Student.requestBook())

        
        elif a == 3:
            centralLibrary.returnBook(Student.returnBook())


        elif a == 4:
            print("Thanks for visiting this library!")
            exit()

        else:
            print("Invalid Choice")
