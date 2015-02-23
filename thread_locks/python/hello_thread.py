# -*- coding: utf-8 -*-

"""Simple 'hello' thread example.
"""

from __future__ import print_function
import threading


def hello():
    print("Hello from new thread")

def main():
    print("Hello from main")
    threading.Thread(target=hello).start()

if __name__ == '__main__':
    main()
