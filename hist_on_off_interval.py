#!/usr/bin/env python

import sys
from os import path
sys.path.append(path.abspath(path.dirname(__file__)))
from on_off_interval import get_on_off_interval

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    data = get_on_off_interval()

    fig, ax = plt.subplots()

    ax.hist(data, bins=max(data) - min(data), normed=True)
    ax.set_xlabel('Interval between ON and OFF states (ms)')
    ax.set_ylabel('Frequency')
    ax.grid()

    fig.savefig('hist_on_off_interval.png', dpi=300,
                bbox_inches='tight', pad_inches=0.2)


if __name__ == '__main__':
    main()
