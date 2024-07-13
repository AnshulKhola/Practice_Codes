class Student:

    def __init__(self,name,major,gpa):
        # name of the student object is equal to the name that is passed in
        self.name = name
        self.major = major
        self.gpa = gpa
        # self.is_on_probation = is_on_probation

    # functions inside a class are called methods
    def on_honour_roll(self):
        if self.gpa >= 8.5:
            return True
        else:
            return False