import numpy as np


def compute_mse(b, w, data):
    x = data[:, 0]
    y = data[:, 1]
    
    y_pred = b + w * x

    mse = np.mean((y - y_pred) ** 2)
    
    return mse



def fit(data, b, w, alpha, num_iterations):

    b_history = []
    w_history = []
    
    n = len(data)
    
    for _ in range(num_iterations):
        x = data[:, 0]
        y = data[:, 1]
        y_pred = b + w * x
        

        gradiente_b = (-2 / n) * np.sum(y - y_pred)
        gradiente_w = (-2 / n) * np.sum(x * (y - y_pred))
        
        b = b - alpha * gradiente_b
        w = w - alpha * gradiente_w
        
        b_history.append(b)
        w_history.append(w)

    return b_history, w_history
