import numpy as np
import scipy
from math import *
#Function for multivariate normal is:
# exp( - 0.5 * (x - m)T * m ** -1 * (x - m)) / sqrt(2 * pi ** rank(c) * det(c))
def timer(function):
    def wrapper(function):
      pass

@timer
def multivariate_normal_logpdf(x, m, c):
  """
  Computes the logarithmic density of a multivariate normal distribution.

  Args:
    x: A numpy array of shape (n, d), where n is the number of data points and d is the dimensionality of the distribution.
    mean: A numpy array of shape (d,) representing the mean of the distribution.
    cov: A numpy array of shape (d, d) representing the covariance matrix of the distribution.

  Returns:
    A numpy array of shape (n,) containing the logarithmic density of each data point.
  """
  
  quad_form = np.einsum('ij,ij->i', x - mean, np.dot(np.linalg.inv(c), x - mean))
  logpdf = -0.5 * (np.log(2 * np.pi) + np.log(np.linalg.det(c)) + quad_form)
  return logpdf


@timer
def using_scipy(m, c, x):
    return scipy.stats.multivariate_normal(m, C).logpdf(x)
