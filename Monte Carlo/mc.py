import type.pattern as pattern
import type.mixpattern as mixpattern

# basic
CCP_NOR, label_nor = pattern.normal_type()
CCP_UT, label_ut = pattern.upward_trend_type()
CCP_DT, label_dt = pattern.downward_trend_type()
CCP_US, label_us = pattern.upward_shift_type()
CCP_DS, label_ds = pattern.downward_shift_type()
CCP_CYC, label_cyc = pattern.cycle_type()
CCP_SYS, label_sys = pattern.systematic_type()
CCP_STR, label_str = pattern.stratification_type()
# mix
CCP_UT_US, label_ut_us = mixpattern.ut_us_type()
CCP_UT_DS, label_ut_ds = mixpattern.ut_ds_type()
CCP_DT_US, label_dt_us = mixpattern.dt_us_type()
CCP_DT_DS, label_dt_ds = mixpattern.dt_ds_type()
CCP_UT_CYC, label_ut_cyc = mixpattern.ut_cyc_type()
CCP_DT_CYC, label_dt_cyc = mixpattern.dt_cyc_type()
print(CCP_UT_US.shape)

