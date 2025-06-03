def lagrange_interpolation(x, y, xi):
    """
    Implementação do método de Lagrange
    """
    stats = {'iterations': 0, 'operations': 0}
    
    n = len(x)
    yi = 0.0
    stats['operations'] += 1
    
    for i in range(n):
        term = y[i]
        stats['operations'] += 1
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
                stats['iterations'] += 1
                stats['operations'] += 4
        yi += term
        stats['operations'] += 1
    
    return yi, stats