import random
import pandas as pd
import numpy as np
import math
mean = 30
sigma = 0.05
time = 25

# normal data
ccp_NOR = []
for j in range(0,200) :
    ccp_nor = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        x_normal = mean + x
        ccp_nor.append(x_normal)
    ccp_NOR.append(ccp_nor)
ccp_NOR = pd.DataFrame(ccp_NOR).to_numpy()
print(ccp_NOR)



# US data
ccp_US = []
for j in range(0, 200):
    ccp_us = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        s = random.uniform(1.5 * sigma, 3 * sigma)
        x_us = mean + x + s
        ccp_us.append(x_us)
    ccp_US.append(ccp_us)
ccp_US = pd.DataFrame(ccp_US).to_numpy()
print(ccp_US)

# DS Data
ccp_DS = []
for j in range(0, 200):
    ccp_ds = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        s = random.uniform(1.5 * sigma, 3 * sigma)
        x_ds = mean + x + s
        ccp_ds.append(x_ds)
    ccp_DS.append(ccp_ds)
ccp_DS = pd.DataFrame(ccp_DS).to_numpy()
print(ccp_DS)

# UT Data
ccp_UT = []
for j in range(0, 200):
    ccp_ut = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        d = random.uniform(0.1 * sigma, 0.3 * sigma)
        x_ut = mean + x + d*i
        ccp_ut.append(x_ut)
    ccp_UT.append(ccp_ut)
ccp_UT = pd.DataFrame(ccp_UT).to_numpy()
print(ccp_UT)


# DT Data
ccp_DT = []
for j in range(0, 200):
    ccp_dt = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        d = random.uniform(0.1 * sigma, 0.3 * sigma)
        x_dt = mean + x + d*i
        ccp_dt.append(x_dt)
    ccp_DT.append(ccp_dt)
ccp_DT = pd.DataFrame(ccp_DT).to_numpy()
print(ccp_DT)

# CYC data
ccp_CYC = []
for j in range(0, 200) :
    ccp_cyc = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        a = random.uniform(1.5 * sigma, 4 * sigma)
        w = random.randint(4, 8)
        x_cyc = mean + x + a * math.sin(2 * math.pi*i/w)
        ccp_cyc.append(x_cyc)
    ccp_CYC.append(ccp_cyc)
ccp_CYC = pd.DataFrame(ccp_CYC).to_numpy()
print(ccp_CYC)

# np.random.seed(777)  不知道要怎用random

