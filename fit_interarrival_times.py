#!/usr/bin/env python

import sys
from os import path
sys.path.append(path.abspath(path.dirname(__file__)))
from interarrival_times import get_interarrival_times
from find_best_fit import find_best_fit


def main():
    data = get_interarrival_times()
    find_best_fit(data)


if __name__ == '__main__':
    main()
