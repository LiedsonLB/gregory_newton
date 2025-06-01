import numpy as np
import time
from math import comb

def gregory_newton_interpolation(x, y, xi):
    """
    Realiza interpolação usando o método de Gregory-Newton para pontos igualmente espaçados
    
    Parâmetros:
    x : array_like - Pontos x conhecidos (deve ser igualmente espaçado)
    y : array_like - Valores y conhecidos correspondentes
    xi : float - Ponto onde se deseja estimar o valor interpolado
    
    Retorna:
    yi : float - Valor interpolado em xi
    table : list - Tabela de diferenças divididas
    """
    
    # Verifica se os pontos x são igualmente espaçados
    h = x[1] - x[0]
    if not np.allclose(np.diff(x), h):
        raise ValueError("Os pontos x devem ser igualmente espaçados para o método Gregory-Newton")
    
    n = len(x)
    if n != len(y):
        raise ValueError("x e y devem ter o mesmo tamanho")
    
    # Tabela de diferenças finitas
    table = [y.copy()]
    for i in range(1, n):
        last_diff = table[-1]
        new_diff = np.diff(last_diff)
        table.append(new_diff)
    
    # Cálculo do valor interpolado de Gregory-Newton
    s = (xi - x[0]) / h
    yi = y[0]
    
    for i in range(1, n):
        combination = 1.0
        for j in range(1, i+1):
            combination *= (s - (j - 1)) / j
        term = table[i][0] * combination
        yi += term
    
    return yi, table

def lagrange_interpolation(x, y, xi):
    """
    Realiza interpolação usando o método de Lagrange
    
    Parâmetros:
    x : array_like - Pontos x conhecidos
    y : array_like - Valores y conhecidos correspondentes
    xi : float - Ponto onde se deseja estimar o valor interpolado
    
    Retorna:
    yi : float - Valor interpolado em xi
    """
    n = len(x)
    if n != len(y):
        raise ValueError("x e y devem ter o mesmo tamanho")
    
    yi = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        yi += term
    
    return yi

def divided_differences(x, y):
    """
    Calcula as diferenças divididas para o método de Newton geral
    
    Parâmetros:
    x : array_like - Pontos x conhecidos
    y : array_like - Valores y conhecidos correspondentes
    
    Retorna:
    table : list - Tabela de diferenças divididas
    """
    n = len(x)
    if n != len(y):
        raise ValueError("x e y devem ter o mesmo tamanho")
    
    table = [y.copy()]
    for i in range(1, n):
        last_diff = table[-1]
        new_diff = np.zeros(n - i)
        for j in range(n - i):
            new_diff[j] = (last_diff[j+1] - last_diff[j]) / (x[j+i] - x[j])
        table.append(new_diff)
    
    return table

def newton_general_interpolation(x, y, xi):
    """
    Realiza interpolação usando o método de Newton (caso geral)
    
    Parâmetros:
    x : array_like - Pontos x conhecidos
    y : array_like - Valores y conhecidos correspondentes
    xi : float - Ponto onde se deseja estimar o valor interpolado
    
    Retorna:
    yi : float - Valor interpolado em xi
    table : list - Tabela de diferenças divididas
    """
    table = divided_differences(x, y)
    n = len(x)
    
    yi = y[0]
    for i in range(1, n):
        term = table[i][0]
        for j in range(i):
            term *= (xi - x[j])
        yi += term
    
    return yi, table

def compare_methods(x, y, xi):
    """
    Compara os três métodos de interpolação
    
    Parâmetros:
    x : array_like - Pontos x conhecidos
    y : array_like - Valores y conhecidos correspondentes
    xi : float - Ponto onde se deseja estimar o valor interpolado
    
    Retorna:
    results : dict - Resultados de cada método com tempo de execução
    """
    results = {}
    
    # Gregory-Newton
    start = time.time()
    try:
        gn_yi, gn_table = gregory_newton_interpolation(x, y, xi)
        results['Gregory-Newton'] = {
            'value': gn_yi,
            'time': time.time() - start,
            'table': gn_table
        }
    except ValueError as e:
        results['Gregory-Newton'] = {
            'error': str(e)
        }
    
    # Lagrange
    start = time.time()
    lag_yi = lagrange_interpolation(x, y, xi)
    results['Lagrange'] = {
        'value': lag_yi,
        'time': time.time() - start
    }
    
    # Newton Geral
    start = time.time()
    ng_yi, ng_table = newton_general_interpolation(x, y, xi)
    results['Newton-Geral'] = {
        'value': ng_yi,
        'time': time.time() - start,
        'table': ng_table
    }
    
    return results

def print_results(results):
    """
    Imprime os resultados da comparação de métodos
    """
    print("\nResultados da Interpolação:")
    print("-" * 50)
    
    for method, data in results.items():
        print(f"\nMétodo: {method}")
        if 'error' in data:
            print(f"  Erro: {data['error']}")
        else:
            print(f"  Valor interpolado: {data['value']}")
            print(f"  Tempo de execução: {data['time']:.6f} segundos")
        
        if 'table' in data:
            print("\n  Tabela de Diferenças:")
            for i, diff in enumerate(data['table']):
                print(f"    Ordem {i}: {diff}")

def main():
    # Exemplo de uso
    print("Interpolação por diferentes métodos\n")
    
    # Dados de exemplo (pontos igualmente espaçados)
    
    x = np.array([0, 1, 2, 3, 4], dtype=float)
    y = np.array([1, 2.5, 3.5, 4.2, 5.0], dtype=float)
    xi = 2.5
    
    print(f"Pontos conhecidos (x, y):")
    for xi_val, yi_val in zip(x, y):
        print(f"  ({xi_val}, {yi_val})")
    print(f"\nPonto a interpolar: x = {xi}")
    
    results = compare_methods(x, y, xi)
    print_results(results)
    
    # Outro exemplo com pontos não igualmente espaçados

    print("\n\nTestando com pontos não igualmente espaçados:")
    x2 = np.array([0, 1, 3, 6, 10], dtype=float)
    y2 = np.array([1, 2.5, 3.5, 4.2, 5.0], dtype=float)

    xi2 = 4.0
    
    print(f"\nPontos conhecidos (x, y):")
    for xi_val, yi_val in zip(x2, y2):
        print(f"  ({xi_val}, {yi_val})")
    print(f"\nPonto a interpolar: x = {xi2}")
    
    results2 = compare_methods(x2, y2, xi2)
    print_results(results2)

if __name__ == "__main__":
    main()