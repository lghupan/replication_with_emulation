#!/usr/bin/env python

import sys
import random
from os import path
sys.path.append(path.abspath(path.dirname(__file__)))
from interarrival_times import get_interarrival_times


def train_lambda():
    data = get_interarrival_times()
    return float(len(data) - 1) / sum(data)


def generate_trace(lambd):
    for run_id in xrange(1, 11):
        curr_ts = 0
        trace = open('poisson_trace_%s' % run_id, 'w')

        while curr_ts < 60000:
            curr_ts += int(round(random.expovariate(lambd)))
            trace.write('%s\n' % curr_ts)

        trace.close()


def main():
    lambd = train_lambda()
    print 'Poisson process lambda:', lambd
    generate_trace(lambd)


if __name__ == '__main__':
    main()
