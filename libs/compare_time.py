from datetime import datetime


def compare_time(time1, time2):
    """Сравнение времени"""
    format = "%H:%M:%S"
    t1 = datetime.strptime(time1, format)
    t2 = datetime.strptime(time2, format)
    return t1 > t2
