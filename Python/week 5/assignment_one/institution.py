    # Initializing a new Class
class Institution:
    def __init__(self, name):
        self.name = name
        self.departments = []
    
    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        return [dept.name for dept in self.departments]