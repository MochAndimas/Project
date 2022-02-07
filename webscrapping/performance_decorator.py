"""performance decorator module"""
from time import time


def performance(func):
    """performance decorator"""
    def wrapper(*args, **kwargs):
        t_1 = time()
        result = func(*args, **kwargs)
        t_2 = time()
        print(f'took {t_2-t_1} s')
        return result
    return wrapper


@performance
def long_time():
    """test1"""
    print("1")
    for i in range(100000000):
        i*5


@performance
def long_time2():
    """test2"""
    print("2")
    for i in list(range(100000000)):
        i*5


if __name__ == "__main__":
    long_time()
    long_time2()
