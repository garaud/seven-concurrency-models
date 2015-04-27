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
        counter.count += 1

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
    main()
