import math
import matplotlib.pyplot as plt
import numpy as np


def sample_uni(theta, n=10000):
    return np.random.uniform(0, theta, n)


def sample_exp(theta, n=10000):
    return np.random.exponential(theta, n)


def est_theta_uni(m_k, k):
    return ((k + 1) * m_k) ** (1 / k)


def est_theta_exp(m_k, k):
    return (m_k / math.factorial(k)) ** (1 / k)


def est_derivation(k, sample, est_theta, theta=1, iters=500):
    derivation = 0
    for i in range(0, iters):
        RVs = sample(theta)
        m_k = np.average([x ** k for x in RVs])
        derivation += (est_theta(m_k, k) - theta) ** 2
    return math.sqrt(derivation / iters)


if __name__ == '__main__':
    dist = [[sample_uni, est_theta_uni], [sample_exp, est_theta_exp]]
    for d in dist:
        span = range(1, 150)
        derivation = [est_derivation(k, d[0], d[1]) for k in span]
        plt.plot(span, derivation)
        plt.title(d[0].__name__)
        plt.xlabel('k')
        plt.show()
