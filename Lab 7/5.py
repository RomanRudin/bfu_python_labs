import numpy as np
import scipy
from math import *
#Function for multivariate normal is:
# exp( - 0.5 * (x - m)T * m ** -1 * (x - m)) / sqrt(2 * pi ** rank(c) * det(c))

np.exp(0 - 0.5 * (x - m).T * np.linalg.inv(m) * (x - m)) / sqrt((2 * pi) ** np.linalg.matrix_rank(c) * np.linalg.det(c))

scipy.stats.multivariate_normal(m, C).logpdf(X)