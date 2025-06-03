import numpy as np

def divided_differences(x, y, stats=None):
    """
    Calcula diferenças divididas para o método de Newton
    """
    if stats is None:
        stats = {'iterations': 0, 'operations': 0}
    
    n = len(x)
    table = [y.copy()]
    stats['operations'] += n
    
    for i in range(1, n):
        last_diff = table[-1]
        new_diff = np.zeros(n - i)
        for j in range(n - i):
            new_diff[j] = (last_diff[j+1] - last_diff[j]) / (x[j+i] - x[j])
            stats['iterations'] += 1
            stats['operations'] += 4
        table.append(new_diff)
    
    return table

def newton_general_interpolation(x, y, xi):
    """
    Implementação do método de Newton (caso geral)
    """
    stats = {'iterations': 0, 'operations': 0}
    
    table = divided_differences(x, y, stats)
    n = len(x)
    
    yi = y[0]
    stats['operations'] += 1
    
    for i in range(1, n):
        term = table[i][0]
        for j in range(i):
            term *= (xi - x[j])
            stats['iterations'] += 1
            stats['operations'] += 2
        yi += term
        stats['operations'] += 1
    
    return yi, table, stats