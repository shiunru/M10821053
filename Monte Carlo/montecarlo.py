import random
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import LabelBinarizer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
mean = 30
sigma = 0.05
time = 25
sample = 200

# normal data
ccp_NOR = []
for j in range(sample):
    ccp_nor = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        x_normal = mean + x
        ccp_nor.append(x_normal)
    ccp_NOR.append(ccp_nor)
ccp_NOR = np.array(ccp_NOR)
ccp_NOR_label = np.full((sample),0)
print(ccp_NOR,ccp_NOR_label)
ccp_NOR_label.shape


# Us data
ccp_US = []

for j in range(sample):
    ccp_us = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        s = random.normalvariate(0, random.uniform(1.5 * sigma, 3 * sigma))
        x_us = mean + x + s

        ccp_us.append(x_us)
    ccp_US.append(ccp_us)
ccp_US = np.array(ccp_US)
ccp_US_label = np.full((sample),1)
print(ccp_US,ccp_US_label)

# DS Data
ccp_DS = []

for j in range(sample):
    ccp_ds = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        s = random.uniform(1.5 * sigma, 3 * sigma)
        x_ds = mean + x + s
        ccp_ds.append(x_ds)
    ccp_DS.append(ccp_ds)
ccp_DS = np.array(ccp_DS)
ccp_DS_label = np.full((sample),2)
print(ccp_DS,ccp_DS_label)


# UT Data
ccp_UT = []
for j in range(sample):
    ccp_ut = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        d = random.uniform(0.1 * sigma, 0.3 * sigma)
        x_ut = mean + x + d*i
        ccp_ut.append(x_ut)
    ccp_UT.append(ccp_ut)
ccp_UT = np.array(ccp_UT)
ccp_UT_label = np.full((sample), 3)
print(ccp_UT,ccp_UT_label)


# DT Data
ccp_DT = []
for j in range(sample):
    ccp_dt = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        d = random.normalvariate(0.1 * sigma, 0.3 * sigma)
        x_dt = mean + x + d*i
        ccp_dt.append(x_dt)
    ccp_DT.append(ccp_dt)
ccp_DT = np.array(ccp_DT)
ccp_DT_label = np.full((sample),4)
print(ccp_DT,ccp_DT_label )


ccp_CYC = []
np.random.seed(777)
for j in range(0, 200) :
    ccp_cyc = []
    for i in range(time):
        x = random.normalvariate(0, sigma)
        a = random.uniform(1.5 * sigma, 4 * sigma)
        w = random.randint(4, 8)
        x_cyc = mean + x + a * math.sin(2 * math.pi*i/w)
        ccp_cyc.append(x_cyc)
    ccp_CYC.append(ccp_cyc)
ccp_CYC = np.array(ccp_CYC)
ccp_CYC_label = np.full((sample),5)
print(ccp_CYC,ccp_CYC_label)

#形成 CCP的DATA 及 LABEL
CCP_label = np.concatenate((ccp_NOR_label, ccp_US_label, ccp_DS_label, ccp_UT_label, ccp_DT_label, ccp_CYC_label), axis=0)
CCP = np.concatenate((ccp_NOR, ccp_US, ccp_DS, ccp_UT, ccp_DT, ccp_CYC), axis=0)

#分為 train  test  75%訓練  25%測試  及 標準化 0~1
CCP_normalize = preprocessing.normalize(CCP, norm='l2')

(trainX, testX, trainY, testY) = train_test_split(CCP_normalize ,
    CCP_label.astype("int"), test_size=0.25, random_state=42)


#處理 label
le = LabelBinarizer()
trainY = le.fit_transform(trainY)
testY = le.transform(testY)


# np.random.seed(777)  不知道要怎用random