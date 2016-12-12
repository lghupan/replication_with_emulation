#!/usr/bin/env python

import collections


def get_on_off_interval():
    # get on off interval
    on_off_interval = []

    log = open('/usr/share/mahimahi/traces/TMobile-LTE-driving.down')

    last_ts = None
    for line in log:
        ts = int(line)
        if last_ts != None and ts != last_ts:
            on_off_interval.append(ts - last_ts)

        last_ts = ts

    log.close()

    return on_off_interval


if __name__ == '__main__':
    data = get_on_off_interval()
    data_cnt = collections.Counter(data)
    
    print 'Interval between two ON states (ms): (interval, occurrence)'
    print sorted(data_cnt.items(), key=lambda x: x[0])
