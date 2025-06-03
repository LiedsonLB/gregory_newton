import time
import numpy as np
import matplotlib.pyplot as plt
from methods.gregory_newton import gregory_newton_interpolation
from methods.lagrange import lagrange_interpolation
from methods.newton_geral import newton_general_interpolation
from utils.data_generator import generate_test_data

def compare_methods(x, y, xi):
    """
    Compara os três métodos de interpolação
    """
    results = {}
    
    # Gregory-Newton
    start = time.time()
    try:
        gn_yi, gn_table, gn_stats = gregory_newton_interpolation(x, y, xi)
        results['Gregory-Newton'] = {
            'value': gn_yi,
            'time': time.time() - start,
            'table': gn_table,
            'stats': gn_stats
        }
    except ValueError as e:
        results['Gregory-Newton'] = {'error': str(e)}
    
    # Lagrange
    start = time.time()
    lag_yi, lag_stats = lagrange_interpolation(x, y, xi)
    results['Lagrange'] = {
        'value': lag_yi,
        'time': time.time() - start,
        'stats': lag_stats
    }
    
    # Newton Geral
    start = time.time()
    ng_yi, ng_table, ng_stats = newton_general_interpolation(x, y, xi)
    results['Newton-Geral'] = {
        'value': ng_yi,
        'time': time.time() - start,
        'table': ng_table,
        'stats': ng_stats
    }
    
    return results

def performance_analysis(max_points=100, step=10):
    """
    Analisa desempenho dos métodos
    """
    point_counts = range(5, max_points+1, step)
    methods = ['Gregory-Newton', 'Lagrange', 'Newton-Geral']
    metrics = {method: {'iterations': [], 'operations': []} for method in methods}
    
    for n in point_counts:
        x_eq, y_eq = generate_test_data(n, 'equal')
        x_rand, y_rand = generate_test_data(n, 'random')
        xi = np.mean(x_eq)
        
        # Testa cada método
        try:
            _, _, gn_stats = gregory_newton_interpolation(x_eq, y_eq, xi)
            metrics['Gregory-Newton']['iterations'].append(gn_stats['iterations'])
            metrics['Gregory-Newton']['operations'].append(gn_stats['operations'])
        except ValueError:
            metrics['Gregory-Newton']['iterations'].append(np.nan)
            metrics['Gregory-Newton']['operations'].append(np.nan)
        
        _, lag_stats = lagrange_interpolation(x_rand, y_rand, xi)
        metrics['Lagrange']['iterations'].append(lag_stats['iterations'])
        metrics['Lagrange']['operations'].append(lag_stats['operations'])
        
        _, _, ng_stats = newton_general_interpolation(x_rand, y_rand, xi)
        metrics['Newton-Geral']['iterations'].append(ng_stats['iterations'])
        metrics['Newton-Geral']['operations'].append(ng_stats['operations'])
    
    # Plotagem dos gráficos
    plt.figure(figsize=(12, 6))
    
    for i, metric in enumerate(['iterations', 'operations']):
        plt.subplot(1, 2, i+1)
        for method in methods:
            plt.plot(point_counts, metrics[method][metric], 'o-', label=method)
        plt.xlabel('Número de pontos')
        plt.ylabel(metric.capitalize())
        plt.title(f'{metric.capitalize()} por Método')
        plt.legend()
        plt.grid(True)
    
    plt.tight_layout()
    plt.show()