import matplotlib.pyplot as plt

def plot_weights(stocks, weights):
    plt.bar(stocks, weights)
    plt.title("Portfolio Allocation")
    plt.show()