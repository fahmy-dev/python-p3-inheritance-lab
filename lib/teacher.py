#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name, knowledge)
        self.knowledge = knowledge

    def teach(self):
        return random.choice(self.knowledge)