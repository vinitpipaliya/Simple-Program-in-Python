import time
class Library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    def displaybook(self):
        print("Books Present in the Library are: ")
        print("-----------------------")
        for i ,item in enumerate(self.books):
            print(f"{i+1} {item}")
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"You have been isuued {bookname}. Please keep it safe and return in 30 days.")
            self.books.remove(bookname)
            return True
        elif bookname ==0:
            None
        else:
            print(f"Sorry, This book in not available right now. Please wait until book is available.")
            return False 
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book safe. Have a great day. Please visit again.")

class Student:
    def requestbook(self):
        self.book=input("Enter a name of the book you want to borrow: ")
        print("-----------------------")
        if self.book.isspace() or len(self.book)==0:
            print("User enter Invalid Character.")
            return 0
        else:
            return self.book
            
    def returnbook(self):
        self.book=input("Enter a book you want to return: ")
        print("-----------------------")
        return self.book
        
if __name__ == "__main__":
    CentralLibrary=Library(["Bhagvad Gita","Shree Krishna","Dental","Programming"])
    student=Student()
    while(True):
        print("-----------------------")
        welcomeMsg='''\n~~~~~ Welcome To Central Library ~~~~~
        Please choose an optrion:
        1. View all the Books
        2. Requsest a Book
        3. Return a Book
        4. Add a book in Library
        5. Exit the Library
        '''
        print(welcomeMsg)
        print("-----------------------")
        try:
            a=int(input("Enter Your choice: "))
            print("-----------------------")
            if a==1:
                CentralLibrary.displaybook()
            elif a==2:
                CentralLibrary.borrowbook(student.requestbook())
            elif a==3:
                CentralLibrary.returnbook(student.returnbook())
            elif a==4:
                CentralLibrary.returnbook(student.returnbook())
            elif a==5:
                print("Do you want to exit?")
                print("-----------------------")
                confirm=input("Press y for yes or n for no : ")
                if confirm.lower()=='y':
                    print("-----------------------")
                    print("Thanks For choosing Central Library.")
                    print("-----------------------")
                    time.sleep(2)
                    exit()
                else:
                    None
            else:
                print("Invalid Choice.")
        except Exception as e:
            print("-----------------------")
            print("Invalid Choice.")