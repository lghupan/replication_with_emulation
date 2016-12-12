#!/usr/bin/env python

import collections


def get_arrivals_per_ms():
    # get arrivals per ms
    arrivals_per_ms = []
    pkts = 0

    log = open('/usr/share/mahimahi/traces/TMobile-LTE-driving.down')

    last_ts = None
    for line in log:
        ts = int(line)
        if ts != last_ts:
            if last_ts != None:
                arrivals_per_ms.append(pkts)
            pkts = 1
        else:
            pkts += 1

        last_ts = ts

    log.close()

    return arrivals_per_ms


if __name__ == '__main__':
    data = get_arrivals_per_ms()
    data_cnt = collections.Counter(data)

    print 'Arrivals per ms: (arrivals_per_ms, occurrence)'
    print sorted(data_cnt.items(), key=lambda x: x[0])
