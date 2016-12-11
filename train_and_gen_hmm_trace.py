#!/usr/bin/env python

import json
import numpy as np
from hmmlearn import hmm


# get arrivals or silence per ms
def get_arrivals_per_ms():
    # read run times
    with open('pantheon_metadata.json') as metadata_file:
        metadata_dict = json.load(metadata_file)
    run_times = metadata_dict['run_times']

    # get arrivals per ms
    arrivals_per_ms = []
    pkts = 0
    last_len = 0
    lengths = []

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

                    for silent_ts in xrange(last_ts + 1, ts):
                        arrivals_per_ms.append(0)

                pkts = 1
            else:
                pkts += 1

            last_ts = ts

        log.close()

        lengths.append(len(arrivals_per_ms) - last_len)
        last_len = len(arrivals_per_ms)

    return arrivals_per_ms, lengths


def train_hmm():
    X, lengths = get_arrivals_per_ms()

    # only allow output to be [0, 20]
    for i in xrange(len(X)):
        if X[i] > 20:
            X[i] = 20

    # in case any output in [0, 20] did not occur
    X += range(0, 22)

    # initialize start probability and transmission matrix
    n_states = 4
    p = 1.0 / n_states
    start_prob = np.ones(n_states) * p
    trans_mat = np.ones((n_states, n_states)) * p

    # initialize emission probability
    n_emissions = 21
    p = 1.0 / n_emissions
    emission_prob = np.ones((n_states, n_emissions)) * p

    # train HMM
    model = hmm.MultinomialHMM(n_components=n_states, n_iter=1000)
    model.startprob_ = start_prob
    model.transmat_ = trans_mat
    model.emissionprob_ = emission_prob

    X = np.array([X])
    model.fit(X.T, lengths)

    return model


def generate_trace(model):
    for run_id in xrange(1, 11):
        X = model.sample(60000)[0]
        trace = open('hmm_trace_%s' % run_id, 'w')

        for ts in xrange(X.size):
            for i in xrange(X[ts]):
                trace.write('%s\n' % ts)

        trace.close()


def main():
    model = train_hmm()
    generate_trace(model)


if __name__ == '__main__':
    main()
