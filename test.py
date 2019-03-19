# 在这个文件中我将尝试引用其他py文件里的函数

import time_sy

if time_sy.compare_time("20190321", "20190320") > 0:
    print("yes")
else:
    print("no")
