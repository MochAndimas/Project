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
