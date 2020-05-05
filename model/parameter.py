import random as rd
import numpy as np
rng = np.random.RandomState(45)
std = 1
class Parameter:
    def __init__(self, mean=0,
                 sd=1,
                 random_noise=rng.uniform(0.2*std, 0.4*std),
                 systematic_departure=rng.uniform(1*std, 3*std),
                 amplitude=rng.uniform(1.5*std, 2.5*std),
                 period=16,
                 gradient=rng.uniform(0.05*std, 0.25*std),
                 shift_magnitude=rng.uniform(1*std, 3*std),
                 shift_position=rng.randint(10, 20)):

        self.mean = mean
        self.sd = sd
        self.random_noise = random_noise
        self.systematic_departure = systematic_departure
        self.amplitude = amplitude
        self.period = period
        self.gradient = gradient
        self.shift_magnitude = shift_magnitude
        self.shift_position = shift_position


class Sample:

    def __init__(self, size=30, number=1):
        self.size = size
        self.number = number

class Weight:

    def __init__(self, w1=0.4, w2=0.6):
        self.w1 = w1
        self.w2 = w2