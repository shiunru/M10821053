import math
import random as rd
import numpy as np

# 基本參數
mean = 50
sigma = 1
sample_size = 25
sample_number = 200


# normal type
def normal_type():
    global mean, sigma, sample_size, sample_number

    CCP_NOR = []
    for i in range(sample_number):
        ccp_nor = []
        for j in range(sample_size):
            x = rd.normalvariate(0, sigma)
            y_normal = mean + x * sigma
            ccp_nor.append(round(y_normal, 3))
        CCP_NOR.append(ccp_nor)
    CCP_NOR = np.array(CCP_NOR)
    label_nor = np.full((sample_number, 1), 1)
    print(CCP_NOR)
    print(label_nor)

# up-ward trend type
def upward_trend_type():
    global mean, sigma, sample_size, sample_number

    CCP_UT = []
    for i in range(sample_number):
        ccp_ut = []
        for j in range(sample_size):
            x = rd.normalvariate(0, sigma)
            g = rd.uniform(0.05*sigma, 0.25*sigma)
            y_ut = mean + x * sigma + g * j
            ccp_ut.append(round(y_ut, 3))
        CCP_UT.append(ccp_ut)
    CCP_UT = np.array(CCP_UT)
    label_ut = np.full((sample_number, 1), 2)
    print(CCP_UT)
    print(label_ut)

# down-ward trend type
def downward_trend_type():
    global mean, sigma, sample_size, sample_number

    CCP_DT = []
    for i in range(sample_number):
        ccp_dt = []
        for j in range(sample_size):
            x = rd.normalvariate(0, sigma)
            g = rd.uniform(0.05*sigma, 0.25*sigma)
            y_dt = mean + x * sigma - g * j
            ccp_dt.append(round(y_dt, 3))
        CCP_DT.append(ccp_dt)
    CCP_DT = np.array(CCP_DT)
    label_dt = np.full((sample_number, 1), 3)
    print(CCP_DT)
    print(label_dt)

# up-ward shift type
def upward_shift_type():
    global mean, sigma, sample_size, sample_number

    CCP_US = []
    for i in range(sample_number):
        ccp_us = []
        for j in range(sample_size):
            x = rd.normalvariate(0, sigma)
            s = rd.uniform(1.5 * sigma, 2.5 * sigma)
            p = 10 and 20
            if j >= p:
                k = 1
            else:
                k = 0
            y_us = mean + x * sigma + s * k
            ccp_us.append(round(y_us, 3))
        CCP_US.append(ccp_us)
    CCP_US = np.array(CCP_US)
    label_us = np.full((sample_number, 1), 4)
    print(CCP_US, label_us)

# down-ward shift type
def downward_shift_type():
    global mean, sigma, sample_size, sample_number

    CCP_DS = []
    for i in range(sample_number):
        ccp_ds = []
        for j in range(sample_size):
            x = rd.normalvariate(0, sigma)
            s = rd.uniform(1.5 * sigma, 2.5 * sigma)
            p = 10 and 20
            if j >= p:
                k = 1
            else:
                k = 0
            y_us = mean + x * sigma - s * k
            ccp_ds.append(round(y_us, 3))
        CCP_DS.append(ccp_ds)
    CCP_DS = np.array(CCP_DS)
    label_ds = np.full((sample_number, 1), 5)
    print(CCP_DS)
    print(label_ds)

# cycle type
def cycle_type():
    global mean, sigma, sample_size, sample_number

    CCP_CYC = []
    for i in range(sample_number):
        ccp_cyc = []
        for j in range(sample_size):
            x = rd.normalvariate(0, sigma)
            a = rd.uniform(1.5 * sigma, 2.5 * sigma)
            w = 16
            y_cyc = mean + x * sigma + a * math.sin(2 * math.pi * j/w)
            ccp_cyc.append(round(y_cyc, 3))
        CCP_CYC.append(ccp_cyc)
    CCP_CYC = np.array(CCP_CYC)
    label_cyc = np.full((sample_number, 1), 6)
    print(CCP_CYC, label_cyc)

# systematic type
def systematic_type():
    global mean, sigma, sample_size, sample_number

    CCP_SYS = []
    for i in range(sample_number):
        ccp_sys = []
        for j in range(sample_size):
            x = rd.normalvariate(0, sigma)
            d = rd.uniform(sigma, 3*sigma)
            y_sys = mean + x + d * -1 * math.sqrt(j)
            ccp_sys.append(round(y_sys, 3))
        CCP_SYS.append(ccp_sys)
    CCP_SYS = np.array(CCP_SYS)
    label_sys = np.full((sample_number, 1), 7)
    print(CCP_SYS)
    print(label_sys)

#
def stratification_type():
    global mean, sigma, sample_size, sample_number

    CCP_STR = []
    for i in range(sample_number):
        ccp_str = []
        for j in range(sample_size):
            x = rd.normalvariate(0, sigma)
            sigma_bar = rd.uniform(0.2 * sigma, 0.4 * sigma)
            y_str = mean + x * sigma_bar
            ccp_str.append(round(y_str, 3))
        CCP_STR.append(ccp_str)
    CCP_STR = np.array(CCP_STR)
    label_str = np.full((sample_number, 1), 8)
    print(CCP_STR)
    print(label_str)