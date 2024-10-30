import numpy as np


def compute_mse(b, w, data):
    x = data[:, 0]
    y = data[:, 1]
    
    y_pred = b + w * x

    mse = np.mean((y - y_pred) ** 2)
    
    return mse


def step_gradient(b, w, data, alpha):

    n = len(data)
    x = data[:, 0]
    y = data[:, 1]
    y_pred = b + w * x

    # Calcula os gradientes
    gradiente_b = (-2 / n) * np.sum(y - y_pred)
    gradiente_w = (-2 / n) * np.sum(x * (y - y_pred))
    
    # Atualiza os valores de b e w
    b = b - alpha * gradiente_b
    w = w - alpha * gradiente_w
    
    return b, w



def fit(data, b, w, alpha, num_iterations):
    """
    Ajusta os parâmetros b e w usando descida de gradiente.
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - valor inicial do bias
    :param w: float - valor inicial do peso
    :param alpha: float - taxa de aprendizado
    :param num_iterations: int - número de iterações para o ajuste
    :return: list, list - listas com o histórico dos valores de b e w ao longo das iterações
    """
    b_history = []
    w_history = []
    
    for _ in range(num_iterations):
        # Executa uma atualização por gradiente descendente usando step_gradient
        b, w = step_gradient(b, w, data, alpha)
        
        # Salva o histórico dos valores de b e w
        b_history.append(b)
        w_history.append(w)

    return b_history, w_history