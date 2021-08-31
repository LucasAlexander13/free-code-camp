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
    experiments = []
    sucesses = 0

    for experiment in range(num_experiments):
        experiment_draw = hat.draw(num_balls_drawn)
        experiments.append(experiment_draw)
        if expected_balls in experiment_draw:
            sucesses += 1
    
    return sucesses / num_experiments

my_hat = Hat(blue=3,red=2,green=6)
experiment(hat=my_hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)