import math
import random as rd
import numpy as np
from model.parameter import Parameter, Sample

# size, number
sample = [Sample()]

# mean, sd, random_noise,systematic_departure,
# amplitude, period, gradient,
# shift_magnitude, shift_position
parameter = [Parameter(50, 1, rd.uniform(0.2, 0.4), rd.uniform(1, 3),
                       rd.uniform(1.5, 2.5), 16, rd.uniform(0.05, 0.25),
                       rd.uniform(1.5, 2.5), 10)]

# NOR
CCP_NOR = []
for i in range(sample[0].number):
    ccp_nor = []
    for j in range(sample[0].size):
        x = rd.normalvariate(0, parameter[0].sd)
        y_normal = parameter[0].mean + x * parameter[0].sd
        ccp_nor.append(round(y_normal, 3))
    CCP_NOR.append(ccp_nor)
CCP_NOR = np.array(CCP_NOR)
label_nor = np.full((sample[0].number, 1), 1)
print(CCP_NOR)
print(label_nor)
CCP_NOR.shape

# UT
CCP_UT = []
for i in range(sample[0].number):
    ccp_ut = []
    for j in range(sample[0].size):
        x = rd.normalvariate(0, parameter[0].sd)
        y_ut = parameter[0].mean + x * parameter[0].sd + parameter[0].gradient * j
        ccp_ut.append(round(y_ut, 3))
    CCP_UT.append(ccp_ut)
CCP_UT = np.array(CCP_UT)
label_ut = np.full((sample[0].number, 1), 2)
print(CCP_UT)
print(label_ut)


# DT
CCP_DT = []
for i in range(sample[0].number):
    ccp_dt = []
    for j in range(sample[0].size):
        x = rd.normalvariate(0, parameter[0].sd)
        y_dt = parameter[0].mean + x * parameter[0].sd - parameter[0].gradient * j
        ccp_dt.append(round(y_dt, 3))
    CCP_DT.append(ccp_dt)
CCP_DT = np.array(CCP_DT)
label_dt = np.full((sample[0].number, 1), 3)
print(CCP_DT)
print(label_dt)

# US
CCP_US = []
for i in range(sample[0].number):
    ccp_us = []
    for j in range(sample[0].size):
        x = rd.normalvariate(0, parameter[0].sd)
        if j >= parameter[0].shift_position:
            k = 1
        else:
            k = 0
        y_us = parameter[0].mean + x * parameter[0].sd + parameter[0].shift_magnitude * k
        ccp_us.append(round(y_us, 3))
    CCP_US.append(ccp_us)
CCP_US = np.array(CCP_US)
label_us = np.full((sample[0].number, 1), 4)
print(CCP_US)
print(label_us)

#DS
CCP_DS = []
for i in range(sample[0].number):
    ccp_ds = []
    for j in range(sample[0].size):
        x = rd.normalvariate(0, parameter[0].sd)
        if j >= parameter[0].shift_position:
            k = 1
        else:
            k = 0
        y_ds = parameter[0].mean + x * parameter[0].sd - parameter[0].shift_magnitude * k
        ccp_ds.append(round(y_ds, 3))
    CCP_DS.append(ccp_ds)
CCP_DS = np.array(CCP_DS)
label_ds = np.full((sample[0].number, 1), 5)
print(CCP_DS)
print(label_ds)

#CYC
CCP_CYC = []
for i in range(sample[0].number):
    ccp_cyc = []
    for j in range(sample[0].size):
        x = rd.normalvariate(0, parameter[0].sd)
        y_cyc = parameter[0].mean + x * parameter[0].sd + parameter[0].amplitude * math.sin((2 * math.pi * j)/parameter[0].period)
        ccp_cyc.append(round(y_cyc, 3))
    CCP_CYC.append(ccp_cyc)
CCP_CYC = np.array(CCP_CYC)
label_cyc = np.full((sample[0].number, 1), 6)
print(CCP_CYC)
print(label_cyc)

# SYS
CCP_SYS = []
for i in range(sample[0].number):
    ccp_sys = []
    for j in range(sample[0].size):
        x = rd.normalvariate(0, parameter[0].sd)
        y_sys = parameter[0].mean + x* parameter[0].sd + parameter[0].systematic_departure * -1 * math.sqrt(j)
        ccp_sys.append(round(y_sys, 3))
    CCP_SYS.append(ccp_sys)
CCP_SYS = np.array(CCP_SYS)
label_sys = np.full((sample[0].number, 1), 7)
print(CCP_SYS)
print(label_sys)

# STR
CCP_STR = []
for i in range(sample[0].number):
    ccp_str = []
    for j in range(sample[0].size):
        x = rd.normalvariate(0, parameter[0].sd)
        y_str = parameter[0].mean + x * parameter[0].random_noise
        ccp_str.append(round(y_str, 3))
    CCP_STR.append(ccp_str)
CCP_STR = np.array(CCP_STR)
label_str = np.full((sample[0].number, 1), 8)
print(CCP_STR)
print(label_str)


