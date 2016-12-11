#!/usr/bin/env python

import sys
from os import path
sys.path.append(path.abspath(path.dirname(__file__)))
from arrivals_per_ms import get_arrivals_per_ms
from find_best_fit import find_best_fit


def main():
    data = get_arrivals_per_ms()
    find_best_fit(data)


if __name__ == '__main__':
    main()
