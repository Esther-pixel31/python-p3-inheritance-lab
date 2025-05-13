#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        if knowledge is None or not isinstance(knowledge, list) or len(knowledge) == 0:
            self.knowledge = ["general pedagogy"]
        else:
            self.knowledge = knowledge

    def teach(self):
        """Returns a random piece of knowledge from the teacher's list."""
        if not self.knowledge:
             raise ValueError("Teacher has no knowledge to teach.")
        return random.choice(self.knowledge)
  
        