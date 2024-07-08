#!/usr/bin/env python3
# Author ID: ykudo

class Student:

    # Define the name and number when a student object is created, ex. student1 = Student('john', 025969102)
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        try:
            return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number)
        except SyntaxError:
            print("Please remove the first 0 from the student number")

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        try:
            self.courses[course] = grade
        except TypeError:
            print("Need 2 arguments")

    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        gpa = 0.0
        #try:
        if len(self.courses) > 0:
            for course in self.courses.keys():
                gpa = gpa + self.courses[course]
                #return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))
                    #continue
            return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))
        else:
            return 'GPA of student ' + self.name + ' is 0.0'
        
        #except (ZeroDivisionError, TypeError):
            #print("Need to enter the courses and grades")

        #return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))
           #print("Need to enter the courses and grades")
           #print('GPA of student ' + self.name + ' is 0.0')

    # Return a list of course that the student passed (not a 0.0 grade)
    def displayCourses(self): 
        #grade = self.courses.values()
        #course = self.courses.keys()
        #pass_course = [i for i in grade if i > 0]
        keys = [k for k, v in self.courses.items() if v > 0]
        return keys
        

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())