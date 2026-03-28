from data_loader import get_data
from model import train_model
from optimizer import optimize
from visualize import plot_weights
import numpy as np

# Load data
data, returns = get_data()

# Prepare features
X = returns.shift(1).dropna()
y = returns.mean(axis=1).shift(-1).dropna()

X = X.iloc[:-1]
y = y.iloc[:-1]

# Train model
model = train_model(X, y)

# Predictions (not used for optimization now)
pred = model.predict(X)

# ✅ FIX: use actual mean returns per stock
mean_returns = returns.mean()

# Covariance matrix
cov_matrix = returns.cov()

# Optimize portfolio
weights = optimize(mean_returns, cov_matrix)

# Plot
stocks = returns.columns
plot_weights(stocks, weights)