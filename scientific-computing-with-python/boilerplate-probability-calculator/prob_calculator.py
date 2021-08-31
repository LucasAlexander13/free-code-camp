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
        if number > len(self.contents):
            return self.contents
        else:
            removed_list = []
    
        for i in range(number):
            removed = random.choice(self.contents)
            removed_list.append(removed)
            
            index = self.contents.index(removed)
            self.contents.pop(index)
        
        return removed_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    sucesses = 0

    for experiment in range(num_experiments):
        experiment_draw = hat.draw(num_balls_drawn)

        good_draw = 0
        total_draw = 0
        for key, value in expected_balls.items():
            total_draw += 1
            draws = experiment_draw.count(key)
            if draws >= value:
                good_draw += 1
        
        if total_draw == good_draw:
            sucesses += 1
        

    return sucesses / num_experiments
