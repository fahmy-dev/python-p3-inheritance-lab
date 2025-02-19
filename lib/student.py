#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name, knowledge)
        self.knowledge = []

    def learn(self, new_knowledge):
        return self.knowledge.append(new_knowledge)
