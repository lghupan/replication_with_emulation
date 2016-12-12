#!/usr/bin/env python

import collections


def get_interarrival_times():
    # get interarrival times
    interarrival_times = []

    log = open('/usr/share/mahimahi/traces/TMobile-LTE-driving.down')

    last_ts = None
    for line in log:
        ts = int(line)
        if last_ts != None:
            interarrival_times.append(ts - last_ts)

        last_ts = ts

    log.close()

    return interarrival_times


if __name__ == '__main__':
    data = get_interarrival_times()
    data_cnt = collections.Counter(data)

    print 'Interarrival times (ms): (interarrival_times, occurrence)'
    print sorted(data_cnt.items(), key=lambda x: x[0])
