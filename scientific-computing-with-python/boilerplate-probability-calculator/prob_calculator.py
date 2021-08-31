import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
