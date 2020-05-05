import type.pattern as type
import numpy as np
from model.parameter import Sample

sample = [Sample()]

CCP_NOR, label_nor = type.normal_type()
CCP_UT, label_ut = type.upward_trend_type()
CCP_DT, label_dt = type.downward_trend_type()
CCP_US, label_us = type.upward_shift_type()
CCP_DS, label_ds = type.downward_shift_type()
CCP_CYC, label_cyc = type.cycle_type()
CCP_SYS, label_sys = type.systematic_type()
CCP_STR, label_str = type.stratification_type()

