import random
import math
mean = 30
sigma = 0.05
time = 25

d = random.uniform(0.1*sigma, 0.3*sigma)


# for i in range(time):
#     x = random.normalvariate(0, sigma)
#     y_normal = mean + x
#     print(y_normal, ' ')

# for i in range(time):
#     x = random.normalvariate(0, sigma)
#     s = random.uniform(1.5 * sigma, 3 * sigma)
#     y_us = mean + x + s
#     print(y_us, ' ')

# for i in range(time):
#     x = random.normalvariate(0, sigma)
#     d = random.uniform(0.1 * sigma, 0.3 * sigma)
#
#     y_ut = mean + x + d*i
#     print(y_ut, ' ')

for i in range(time):
    x = random.normalvariate(0, sigma)
    a = random.uniform(1.5 * sigma, 4 * sigma)
    w = random.randint(4, 8)
    y_cyc = mean + x + a * math.sin(2 * math.pi*i/w)
    print(y_cyc)
    #1