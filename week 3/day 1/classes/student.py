class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []


    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        else:
            return 0

    def __str__(self):
        return f'{self.name} (average {self.average()})'