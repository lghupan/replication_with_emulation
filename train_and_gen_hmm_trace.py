#!/usr/bin/env python

import numpy as np
from hmmlearn import hmm


# get arrivals or silence per ms
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

                for silent_ts in xrange(last_ts + 1, ts):
                    arrivals_per_ms.append(0)

            pkts = 1
        else:
            pkts += 1

        last_ts = ts

    log.close()

    return arrivals_per_ms


def train_hmm():
    X = get_arrivals_per_ms()

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
    model.fit(X.T)

    return model


def generate_trace(model):
    for run_id in xrange(1, 11):
        X = model.sample(60000)[0]
        trace = open('hmm_trace_%s' % run_id, 'w')

        for ts in xrange(X.size):
            for i in xrange(X[ts][0]):
                trace.write('%s\n' % ts)

        trace.close()


def main():
    model = train_hmm()
    generate_trace(model)


if __name__ == '__main__':
    main()
