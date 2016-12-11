#!/usr/bin/env python

import sys
from os import path
sys.path.append(path.abspath(path.dirname(__file__)))
from arrivals_per_ms import get_arrivals_per_ms

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    data = get_arrivals_per_ms()

    fig, ax = plt.subplots()

    ax.hist(data, bins=max(data) - min(data), normed=True)
    ax.set_xlabel('Arrivals per ms')
    ax.set_ylabel('Frequency')
    ax.grid()

    fig.savefig('hist_arrivals_per_ms.png', dpi=300,
                bbox_inches='tight', pad_inches=0.2)


if __name__ == '__main__':
    main()
