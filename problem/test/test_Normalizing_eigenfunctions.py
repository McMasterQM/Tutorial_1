from ..Normalizing_eigenfunctions import *

import numpy as np
from numpy.testing import assert_equal, assert_allclose
from scipy.integrate import quad
from functools import partial


def compute_probability(x, n, a):
    """Compute 1-dimensional particle-in-a-box probablity value(s).

    See `compute_wavefunction` parameters.
    """
    return compute_wavefunction(x, n, a) ** 2

def test_compute_wavefunction():
    """
    testing compute_wavefunction function
    :return:
    """
    n = np.random.randint(100,  size=10)
    a = np.random.rand(10)*10

    for n_, a_ in zip(n, a):
        wfn_sqr = partial(compute_probability, n=int(n_), a=a_)
        res, err = quad(wfn_sqr, 0, a_)
        assert_allclose(res, np.ones(1))