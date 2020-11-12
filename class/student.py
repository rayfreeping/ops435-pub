#!/usr/bin/env python3
# Author: Raymond Chan
# For: OPS435 - Python Class Example
class Student:
    ''' Here is the docstring for the Student Class.
        This is the blueprint for creating a student instance.
        To use this blueprint, you need to provide
        (a) a name for the student as string,
        (b) a student ID number for the student also as a string.
        
        e.g. student1 = Student('john', '0123456789')
        A new student type object will be returned.
        '''
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Display student number and number
    def displayInfo(self):
        '''Concatencate the student name and student number 
           and return it to the caller as a string.'''
        StudentInfo = self.name + '\n' + self.number
        return StudentInfo

    def showInfo(self):
        '''Send the student name and the student number to the standard output.'''
        print(self.name)
        print(self.number)

    # Add a new course and grade to student record
    def addGrade(self, course, grade):
        '''This object method take a course name as a string,
           and the grade for the given course as a number.
           the given grade will be add to the course dictionay
           as an item with course as the key and grade as the
           value.'''
        self.courses[course] = grade

    # Calculate the grade point average of all courses and return it
    def displayGPA(self):
        '''Thie object method computer the grade point average for
           for the course/grade stored in the course dictionary
           and return the gpa as a floating point object.'''
        gpa = 0.0
        for course in self.courses.keys():
            gpa = gpa + self.courses[course]
        if len(self.courses) > 0:
            return gpa / len(self.courses)
        else:
            return 0
