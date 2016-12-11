#!/usr/bin/env python

import sys
from os import path
sys.path.append(path.abspath(path.dirname(__file__)))
from on_off_interval import get_on_off_interval
from find_best_fit import find_best_fit


def main():
    data = get_on_off_interval()
    find_best_fit(data)


if __name__ == '__main__':
    main()
