import numpy as np

def generate_test_data(n_points, spacing='equal'):
    """
    Gera dados sintéticos para testes
    
    Parâmetros:
    n_points : int - Número de pontos
    spacing : str - 'equal' (igual) ou 'random' (aleatório)
    
    Retorna:
    tuple: (array_x, array_y) - Arrays NumPy com valores gerados
    """
    if spacing == 'equal':
        x = np.linspace(0, 2*np.pi, n_points)
    else:
        x = np.sort(np.random.uniform(0, 2*np.pi, n_points))
    
    y = np.sin(x) + np.cos(2*x)
    return x, y