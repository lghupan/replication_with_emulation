import json


def get_on_off_interval():
    # read run times
    with open('pantheon_metadata.json') as metadata_file:
        metadata_dict = json.load(metadata_file)
    run_times = metadata_dict['run_times']

    # get on off interval
    on_off_interval = []

    for run_id in xrange(1, 1 + run_times):
        log = open('default_tcp_datalink_run%s.log' % run_id)

        last_ts = None
        for line in log:
            items = line.split()
            if len(items) < 4 or items[1] != '-':
                continue

            ts = int(items[0])
            if last_ts != None and ts != last_ts:
                on_off_interval.append(ts - last_ts)

            last_ts = ts

        log.close()

    return on_off_interval
