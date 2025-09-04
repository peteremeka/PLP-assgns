from institution import Institution
from book import Book
from department import Computer, Engineering

institution = Institution("University of Nigeria Nsukka")

    # Create department
computer = Computer()
engineering = Engineering()

institution.add_department(computer)
institution.add_department(engineering)

    # Create Books
bk_comp_one = Book("Introduction to Python Programming", "2nd", "Peter Ekwelike \n")
bk_comp_two = Book("Introduction to Database Management System", "4th", "Jim Mckerson \n")
bk_comp_three = Book("Introduction to Web Development", "3rd", "Michael Erikson")

bk_eng = Book("Introduction to Mechanical Engineering", "1st", "Jeffery George")

    # Add Books to Departments
computer.add_book(bk_comp_one)
computer.add_book(bk_comp_two)
computer.add_book(bk_comp_three)
engineering.add_book(bk_eng)

print("\n")
print("Departments in", institution.name, ":", institution.show_departments())
print("Computer Books:", computer.get_books())
print("Engineering Books:", engineering.get_books())
print("\n")
