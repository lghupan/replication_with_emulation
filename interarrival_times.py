def get_interarrival_times():
    # get interarrival times
    interarrival_times = []

    log = open('/usr/share/mahimahi/traces/Verizon-LTE-driving.down')

    last_ts = None
    for line in log:
        ts = int(line)
        if last_ts != None:
            interarrival_times.append(ts - last_ts)

        last_ts = ts

    log.close()

    return interarrival_times
