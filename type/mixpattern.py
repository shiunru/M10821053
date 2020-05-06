import numpy as np
from model.parameter import Parameter, Sample, Weight

rng = np.random.RandomState(45)
sample = [Sample()]
parm = [Parameter()]
w = [Weight()]


# UT+US
def ut_us_type():
    CCP_UT_US = []
    for i in range(sample[0].number):
        ccp_ut_us = []
        for j in range(sample[0].size):
            x = round(rng.normal(0, parm[0].sd), 3)
            if j % 2 == 0:
                if j >= parm[0].shift_position:
                    k = 1
                else:
                    k = 0
                y_ut_us = (w[0].four * (parm[0].mean + x * parm[0].sd + parm[0].shift_magnitude * k)
                           + w[0].six * (parm[0].mean + x * parm[0].sd + parm[0].gradient * j))
            else:
                if j >= parm[0].shift_position:
                    k = 1
                else:
                    k = 0
                y_ut_us = (w[0].six * (parm[0].mean + x * parm[0].sd + parm[0].shift_magnitude * k)
                           + w[0].four * (parm[0].mean + x * parm[0].sd + parm[0].gradient * j))
            ccp_ut_us.append(round(y_ut_us, 3))
        CCP_UT_US.append(ccp_ut_us)
    CCP_UT_US = np.array(CCP_UT_US)
    label_ut_us = np.full((sample[0].number, 1), 9)
    return CCP_UT_US, label_ut_us


# UT+DS
def ut_ds_type():
    CCP_UT_DS = []
    for i in range(sample[0].number):
        ccp_ut_ds = []
        for j in range(sample[0].size):
            x = round(rng.normal(0, parm[0].sd), 3)
            if j % 2 == 0:
                if j >= parm[0].shift_position:
                    k = 1
                else:
                    k = 0
                y_ut_ds = (w[0].four * (parm[0].mean + x * parm[0].sd - parm[0].shift_magnitude * k)
                           + w[0].six * (parm[0].mean + x * parm[0].sd + parm[0].gradient * j))
            else:
                if j >= parm[0].shift_position:
                    k = 1
                else:
                    k = 0
                y_ut_ds = (w[0].six * (parm[0].mean + x * parm[0].sd - parm[0].shift_magnitude * k)
                           + w[0].four * (parm[0].mean + x * parm[0].sd + parm[0].gradient * j))
            ccp_ut_ds.append(round(y_ut_ds, 3))
        CCP_UT_DS.append(ccp_ut_ds)
    CCP_UT_DS = np.array(CCP_UT_DS)
    label_ut_ds = np.full((sample[0].number, 1), 10)
    return CCP_UT_DS, label_ut_ds


# DT+US
def dt_us_type():
    CCP_DT_US = []
    for i in range(sample[0].number):
        ccp_dt_us = []
        for j in range(sample[0].size):
            x = round(rng.normal(0, parm[0].sd), 3)
            if j % 2 == 0:
                if j >= parm[0].shift_position:
                    k = 1
                else:
                    k = 0
                y_dt_us = (w[0].four * (parm[0].mean + x * parm[0].sd + parm[0].shift_magnitude * k)
                           + w[0].six * (parm[0].mean + x * parm[0].sd - parm[0].gradient * j))
            else:
                if j >= parm[0].shift_position:
                    k = 1
                else:
                    k = 0
                y_dt_us = (w[0].six * (parm[0].mean + x * parm[0].sd + parm[0].shift_magnitude * k)
                           + w[0].four * (parm[0].mean + x * parm[0].sd - parm[0].gradient * j))
            ccp_dt_us.append(round(y_dt_us, 3))
        CCP_DT_US.append(ccp_dt_us)
    CCP_DT_US = np.array(CCP_DT_US)
    label_dt_us = np.full((sample[0].number, 1), 11)
    return CCP_DT_US, label_dt_us


# DT+DS
def dt_ds_type():
    CCP_DT_DS = []
    for i in range(sample[0].number):
        ccp_dt_ds = []
        for j in range(sample[0].size):
            x = round(rng.normal(0, parm[0].sd), 3)
            if j % 2 == 0:
                if j >= parm[0].shift_position:
                    k = 1
                else:
                    k = 0
                y_dt_ds = (w[0].four * (parm[0].mean + x * parm[0].sd - parm[0].shift_magnitude * k)
                           + w[0].six * (parm[0].mean + x * parm[0].sd - parm[0].gradient * j))
            else:
                if j >= parm[0].shift_position:
                    k = 1
                else:
                    k = 0
                y_dt_ds = (w[0].six * (parm[0].mean + x * parm[0].sd - parm[0].shift_magnitude * k)
                           + w[0].four * (parm[0].mean + x * parm[0].sd - parm[0].gradient * j))
            ccp_dt_ds.append(round(y_dt_ds, 3))
        CCP_DT_DS.append(ccp_dt_ds)
    CCP_DT_DS = np.array(CCP_DT_DS)
    label_dt_ds = np.full((sample[0].number, 1), 12)
    return CCP_DT_DS, label_dt_ds


# UT+CYC
def ut_cyc_type():
    CCP_UT_CYC = []
    for i in range(sample[0].number):
        ccp_ut_cyc = []
        for j in range(sample[0].size):
            x = round(rng.normal(0, parm[0].sd), 3)
            if j % 2 == 0:
                y_ut_cyc = (w[0].four * (parm[0].mean + x * parm[0].sd + parm[0].gradient * j)
                            + w[0].six * (parm[0].mean + x * parm[0].sd + parm[0].amplitude * np.sin(
                            (2 * np.pi * j) / parm[0].period)))
            else:
                y_ut_cyc = (w[0].six * (parm[0].mean + x * parm[0].sd + parm[0].gradient * j)
                            + w[0].four * (parm[0].mean + x * parm[0].sd + parm[0].amplitude * np.sin(
                            (2 * np.pi * j) / parm[0].period)))
            ccp_ut_cyc.append(round(y_ut_cyc, 3))
        CCP_UT_CYC.append(ccp_ut_cyc)
    CCP_UT_CYC = np.array(CCP_UT_CYC)
    label_ut_cyc = np.full((sample[0].number, 1), 13)
    return CCP_UT_CYC, label_ut_cyc


# DT+CYC
def dt_cyc_type():
    CCP_DT_CYC = []
    for i in range(sample[0].number):
        ccp_dt_cyc = []
        for j in range(sample[0].size):
            x = round(rng.normal(0, parm[0].sd), 3)
            if j % 2 == 0:
                y_dt_cyc = (w[0].four * (parm[0].mean + x * parm[0].sd - parm[0].gradient * j)
                            + w[0].six * (parm[0].mean + x * parm[0].sd + parm[0].amplitude * np.sin(
                            (2 * np.pi * j) / parm[0].period)))
            else:
                y_dt_cyc = (w[0].six * (parm[0].mean + x * parm[0].sd - parm[0].gradient * j)
                            + w[0].four * (parm[0].mean + x * parm[0].sd + parm[0].amplitude * np.sin(
                            (2 * np.pi * j) / parm[0].period)))
            ccp_dt_cyc.append(round(y_dt_cyc, 3))
        CCP_DT_CYC.append(ccp_dt_cyc)
    CCP_DT_CYC = np.array(CCP_DT_CYC)
    label_dt_cyc = np.full((sample[0].number, 1), 14)
    return CCP_DT_CYC, label_dt_cyc
