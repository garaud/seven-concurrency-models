# coding: utf-8

"""Example of shared data and race condition with a simple counter which is
incremented by two threads.
"""

from __future__ import print_function
import threading

MAX_ITER = 5000

Counter = type("Counter", (object,), {'count': 0})

def increment_loop(counter):
    for _ in range(MAX_ITER):
        counter.count = counter.count + 1

def main():
    counter = Counter()
    t1 = threading.Thread(target=increment_loop, args=(counter,))
    t2 = threading.Thread(target=increment_loop, args=(counter,))
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print("Counter value '{}'".format(counter.count))

if __name__ == '__main__':
    # This forces to have more context switching to reproduce a data race in
    # Python 2 and Python 3 respectively.
    import sys
    if sys.version_info.major == 2:
        sys.setcheckinterval(20)
    else:
        # No more ticks in Python 3, it's time based.
        # 0.05 millisecond, 1000 times smaller than the default (5 milliseconds)
        sys.setswitchinterval(5e-5)
    main()
