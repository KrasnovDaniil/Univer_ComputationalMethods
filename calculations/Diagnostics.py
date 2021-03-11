import time

def time_check(func):
    start = time.time()
    func()
    finish = time.time()
    return finish - start