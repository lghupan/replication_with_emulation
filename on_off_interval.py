def get_on_off_interval():
    # get on off interval
    on_off_interval = []

    log = open('/usr/share/mahimahi/traces/Verizon-LTE-driving.down')

    last_ts = None
    for line in log:
        ts = int(line)
        if last_ts != None and ts != last_ts:
            on_off_interval.append(ts - last_ts)

        last_ts = ts

    log.close()

    return on_off_interval
