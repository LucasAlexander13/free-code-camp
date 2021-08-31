import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        removed_list = []
        for i in range(number):
            removed = random.choice(self.contents)
            removed_list.append(removed)
            
            index = self.contents.index(removed)
            self.contents.pop(index)
        
        return removed_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
