import numpy as np
import scipy
from time import perf_counter

def timer(function):
    def wrapper(*args, **kwargs):
        start = perf_counter() 
        result = function(*args, **kwargs) 
        end = perf_counter() 
        print(f'Function {function.__name__} executed in {(end-start)}s') 
        return result 
    return wrapper 

@timer
def multivariate_normal_logpdf(x: np.array, m: np.array, c: np.array) -> np.array:
  quad_form = np.einsum('ij,ij->i', x - m, np.dot(np.linalg.inv(c), x - m))
  logpdf = -0.5 * (np.log(2 * np.pi) + np.log(np.linalg.det(c)) + quad_form)
  return logpdf

@timer
def using_scipy(x: np.array, m: np.array, c: np.array) -> np.array:
    return scipy.stats.multivariate_normal(m, c).logpdf(x)


x = np.array([[1, 2], [3, 4]])
m = np.array([0, 0])
c = np.array([[1, 0.5], [0.5, 2]])


result1 = multivariate_normal_logpdf(x, m, c)
print(f"The result of my function is: {result1}")
print()
result2 = using_scipy(x, m, c)
print(f"The result of function using scipy is: {result2}")
print()
difference = np.array(abs((result2 - result1) / result1))
print(f"Difference between those two answers (on average) is {difference.sum() / len(difference)} parts of the first result.")