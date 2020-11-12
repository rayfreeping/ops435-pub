#!/usr/bin/env python3
class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}
        
    def displayInfo(self):
        Return self.name+'\n'+self.number
        
    def addGrade(self, course, grade):
        self.courses[course] = grade     
