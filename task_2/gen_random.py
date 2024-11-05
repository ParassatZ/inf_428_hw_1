import numpy as np

def generate_random_data(mean, variance, num_samples):
    low = max(mean - variance, 0)
    high = min(mean + variance + 1, 90)

    if low >= high:
        return np.full(num_samples, mean)
    
    return np.random.randint(low, high, num_samples)

