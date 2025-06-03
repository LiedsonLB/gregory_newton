import numpy as np

def gregory_newton_interpolation(x, y, xi):
    """
    Implementação do método Gregory-Newton para pontos igualmente espaçados
    """
    stats = {'iterations': 0, 'operations': 0}
    
    h = x[1] - x[0]
    if not np.allclose(np.diff(x), h):
        raise ValueError("Pontos x devem ser igualmente espaçados")
    
    n = len(x)
    table = [y.copy()]
    stats['operations'] += n
    
    for i in range(1, n):
        last_diff = table[-1]
        new_diff = np.diff(last_diff)
        table.append(new_diff)
        stats['iterations'] += 1
        stats['operations'] += len(last_diff) - 1
    
    s = (xi - x[0]) / h
    yi = y[0]
    stats['operations'] += 2
    
    for i in range(1, n):
        combination = 1.0
        for j in range(1, i+1):
            combination *= (s - (j - 1)) / j
            stats['iterations'] += 1
            stats['operations'] += 3
        term = table[i][0] * combination
        yi += term
        stats['operations'] += 2
    
    return yi, table, stats