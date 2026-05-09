import matplotlib.pyplot as plt

def plot_results(betas_A, betas_B, beta_true):
    plt.scatter(betas_A[:, 0], betas_A[:, 1], alpha=0.4, label="rho=0")
    plt.scatter(betas_B[:, 0], betas_B[:, 1], alpha=0.4, label="rho=0.99")

    plt.scatter(beta_true[0], beta_true[1], color='red', label="True Beta")

    plt.xlabel("beta1")
    plt.ylabel("beta2")
    plt.legend()
    plt.show()