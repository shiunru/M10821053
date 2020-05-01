class Parameter:

    def __init__(self, mean, sd, random_noise,
                 systematic_departure, amplitude, period,
                 gradient, shift_magnitude, shift_position):
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

    def __init__(self, size=25, number=200):
        self.size = size
        self.number = number
