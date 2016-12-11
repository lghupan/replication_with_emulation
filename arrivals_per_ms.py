def get_arrivals_per_ms():
    # get arrivals per ms
    arrivals_per_ms = []
    pkts = 0

    log = open('/usr/share/mahimahi/traces/Verizon-LTE-driving.down')

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
