# -*- coding: utf-8 -*-
# 在这个文件中我将尝试引用其他py文件里的函数

import time_sy

'''
# 测试compare_time的功能
if time_sy.compare_time("20190321", "20190320") > 0:
    print("yes")
else:
    print("no")
'''

all_payday = time_sy.get_all_payday("19980817",12)
for i in all_payday:
    print i