import numpy as np

def generate_X(n=100, rho=0.0):
    x1 = np.random.normal(0, 1, n)
    z = np.random.normal(0, 1, n)
    x2 = rho * x1 + np.sqrt(1 - rho**2) * z
    X = np.column_stack([x1, x2])
    return X