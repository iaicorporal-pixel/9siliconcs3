class publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    def display(self):
        print(f"Title: {self.__title}, Author: {self.__author}")

class book(publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.__pages = pages if pages > 0 else print("The number of pages must be positive")
    def display(self):
        super().display()
        print(f"Pages: {self.__pages}")

class magazine(publication):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue 
    def display(self):
        print(f"Title: {self.__title}, Issue: {self.issue}")

for item in [publication("Pub1", "AuthA"), book("Book1", "AuthB", -5), magazine("Mag1", "AuthC", 4)]:
    item.display()
    print("-" * 10)