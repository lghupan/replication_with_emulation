#!/usr/bin/env python
import random

total_time = 1000 * 60  # 60 sec trace
cur_time = 1  # 

cur_packets_per_ms = random.random()

# every 100ms decide how many departure events to have
with open('randwalk_trace.log', 'w') as trace:
    while cur_time < total_time:
        if random.random() > cur_packets_per_ms:
            trace.write('%d\n' % cur_time)

        probability_delta = .015
        if random.getrandbits(1):
            cur_packets_per_ms += probability_delta
        else:
            cur_packets_per_ms -= probability_delta

        cur_packets_per_ms = min(cur_packets_per_ms, 1.)
        cur_packets_per_ms = max(cur_packets_per_ms, 0.)
        cur_time += 1
