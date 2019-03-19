import time


def compare_time(time1, time2):
    # 输入的时间是"YYYYMMDD"8位数字格式
    # 前后时间相同 = 0
    # 前面的时间比后面的时间晚 > 0的结果
    # 前面的时间比后面的时间早 < 0的结果
    s_time = time.mktime(time.strptime(time1, '%Y%m%d'))
    e_time = time.mktime(time.strptime(time2, '%Y%m%d'))
    return int(s_time) - int(e_time)

