class Publication:
    def __init__(self, title, author):
        self.__title = title     
        self.__author = author    
        
    def show_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)

class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        
        if pages <= 0:
            print("The number of pages must be positive")
            self.__pages = 0  
        else:
            self.__pages = pages

    def show_info(self):
        super().show_info()
        print("Pages:", self.__pages)

class Magazine(Publication):
    def __init__(self, title, author, issue_no):
        super().__init__(title, author)
        self.issue = issue_no  

    def display_mag(self):     
        print("Mag Name:", self.__title) 
        print("Issue:", self.issue)