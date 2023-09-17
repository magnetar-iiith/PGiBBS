# get BayesianPrivacyAccountant from https://github.com/AlekseiTriastcyn/bayesian-differential-privacy/tree/master

from bayesian_privacy_accountant import BayesianPrivacyAccountant
import sys
import numpy as np

accountant = BayesianPrivacyAccountant(powers=100, bayesianDP=False)
accountant.accumulate(
    ldistr=(0.0, float(sys.argv[1]) * float(sys.argv[2])),
    rdistr=(float(sys.argv[2]), float(sys.argv[1]) * float(sys.argv[2])),
    q=0.2,     # sampling probability
    steps=50 # number of iterations
)

print(accountant.get_privacy(target_delta=1e-2))
