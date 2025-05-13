#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, new_knowledge):
        """Add new knowledge (a string) to the student's list."""
        if isinstance(new_knowledge, str):
            self.knowledge.append(new_knowledge)
        else:
            raise TypeError("Student can only learn from string input.")