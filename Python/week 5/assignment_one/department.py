        # Initializing a new Class
class Department:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def get_books(self):
        return [bk.name for bk in self.books]


        # Initializing an Two "INHERITANCE"
class Computer(Department):
    def __init__(self):
        super().__init__("Computer Science")

class Engineering(Department):
    def __init__(self):
        super().__init__("Mechanical Engineering")

