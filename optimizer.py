import numpy as np
from scipy.optimize import minimize

def optimize(mean_returns, cov_matrix):

    def sharpe(weights):
        ret = np.dot(weights, mean_returns)
        risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        return -ret / risk

    num_assets = len(mean_returns)
    constraints = ({'type': 'eq', 'fun': lambda x: sum(x) - 1})
    bounds = tuple((0,1) for _ in range(num_assets))

    init = num_assets * [1./num_assets]

    result = minimize(sharpe, init, method='SLSQP',
                      bounds=bounds, constraints=constraints)

    return result.x