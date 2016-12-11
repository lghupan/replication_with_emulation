import json


def get_arrivals_per_ms():
    # read run times
    with open('pantheon_metadata.json') as metadata_file:
        metadata_dict = json.load(metadata_file)
    run_times = metadata_dict['run_times']

    # get arrivals per ms
    arrivals_per_ms = []
    pkts = 0

    for run_id in xrange(1, 1 + run_times):
        log = open('default_tcp_datalink_run%s.log' % run_id)

        last_ts = None
        for line in log:
            items = line.split()
            if len(items) < 4 or items[1] != '-':
                continue

            ts = int(items[0])
            if ts != last_ts:
                if last_ts:
                    arrivals_per_ms.append(pkts)
                pkts = 1
            else:
                pkts += 1

            last_ts = ts

        log.close()

    return arrivals_per_ms
