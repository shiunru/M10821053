import numpy as np
from model.parameter import Parameter, Sample
rng = np.random.RandomState(45)
sample = [Sample()]
parm = [Parameter()]

# normal type
def normal_type():
    CCP_NOR = []
    for i in range(sample[0].number):
        ccp_nor = []
        for j in range(sample[0].size):
            x = round(rng.normal(0, parm[0].sd), 2)
            y_normal = parm[0].mean + x * parm[0].sd
            ccp_nor.append(round(y_normal, 3))
        CCP_NOR.append(ccp_nor)
    CCP_NOR = np.array(CCP_NOR)
    label_nor = np.full((sample[0].number, 1), 1)
    return CCP_NOR, label_nor
    CCP_NOR.shape


# up-ward trend type
def upward_trend_type():
    CCP_UT = []
    for i in range(sample[0].number):
        ccp_ut = []
        for j in range(sample[0].size):
            x = rng.normal(0, parm[0].sd)
            y_ut = parm[0].mean + x * parm[0].sd + parm[0].gradient * j
            ccp_ut.append(round(y_ut, 3))
        CCP_UT.append(ccp_ut)
    CCP_UT = np.array(CCP_UT)
    label_ut = np.full((sample[0].number, 1), 2)
    return CCP_UT, label_ut


# down-ward trend type
def downward_trend_type():
    CCP_DT = []
    for i in range(sample[0].number):
        ccp_dt = []
        for j in range(sample[0].size):
            x = rng.normal(0, parm[0].sd)
            y_dt = parm[0].mean + x * parm[0].sd - parm[0].gradient * j
            ccp_dt.append(round(y_dt, 3))
        CCP_DT.append(ccp_dt)
    CCP_DT = np.array(CCP_DT)
    label_dt = np.full((sample[0].number, 1), 3)
    return CCP_DT, label_dt


# up-ward shift type
def upward_shift_type():
    CCP_US = []
    for i in range(sample[0].number):
        ccp_us = []
        for j in range(sample[0].size):
            x = rng.normal(0, parm[0].sd)
            if j >= parm[0].shift_position:
                k = 1
            else:
                k = 0
            y_us = parm[0].mean + x * parm[0].sd + parm[0].shift_magnitude * k
            ccp_us.append(round(y_us, 3))
        CCP_US.append(ccp_us)
    CCP_US = np.array(CCP_US)
    label_us = np.full((sample[0].number, 1), 4)
    return CCP_US, label_us


# down-ward shift type
def downward_shift_type():
    CCP_DS = []
    for i in range(sample[0].number):
        ccp_ds = []
        for j in range(sample[0].size):
            x = rng.normal(0, parm[0].sd)
            if j >= parm[0].shift_position:
                k = 1
            else:
                k = 0
            y_ds = parm[0].mean + x * parm[0].sd - parm[0].shift_magnitude * k
            ccp_ds.append(round(y_ds, 3))
        CCP_DS.append(ccp_ds)
    CCP_DS = np.array(CCP_DS)
    label_ds = np.full((sample[0].number, 1), 5)
    return CCP_DS, label_ds


# cycle type
def cycle_type():
    CCP_CYC = []
    for i in range(sample[0].number):
        ccp_cyc = []
        for j in range(sample[0].size):
            x = rng.normal(0, parm[0].sd)
            y_cyc = parm[0].mean + x * parm[0].sd + parm[0].amplitude * np.sin(
                (2 * np.pi * j) / parm[0].period)
            ccp_cyc.append(round(y_cyc, 3))
        CCP_CYC.append(ccp_cyc)
    CCP_CYC = np.array(CCP_CYC)
    label_cyc = np.full((sample[0].number, 1), 6)
    return CCP_CYC, label_cyc


# systematic type
def systematic_type():
    CCP_SYS = []
    for i in range(sample[0].number):
        ccp_sys = []
        for j in range(sample[0].size):
            x = rng.normal(0, parm[0].sd)
            y_sys = parm[0].mean + x * parm[0].sd + parm[0].systematic_departure * np.power(-1, j)
            ccp_sys.append(round(y_sys, 3))
        CCP_SYS.append(ccp_sys)
    CCP_SYS = np.array(CCP_SYS)
    label_sys = np.full((sample[0].number, 1), 7)
    return CCP_SYS, label_sys


# stratification type
def stratification_type():
    CCP_STR = []
    for i in range(sample[0].number):
        ccp_str = []
        for j in range(sample[0].size):
            x = rng.normal(0, parm[0].sd)
            y_str = parm[0].mean + x * parm[0].random_noise
            ccp_str.append(round(y_str, 3))
        CCP_STR.append(ccp_str)
    CCP_STR = np.array(CCP_STR)
    label_str = np.full((sample[0].number, 1), 8)
    return CCP_STR, label_str



