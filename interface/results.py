def print_results(results):
    """
    Imprime os resultados da comparação formatados
    """
    print("\nResultados da Interpolação:")
    print("-" * 70)
    
    for method, data in results.items():
        print(f"\nMétodo: {method}")
        if 'error' in data:
            print(f"  Erro: {data['error']}")
        else:
            print(f"  Valor interpolado: {data['value']:.8f}")
            print(f"  Tempo de execução: {data['time']:.6f} segundos")
            print(f"  Iterações: {data['stats']['iterations']}")
            print(f"  Operações: {data['stats']['operations']}")
        
        if 'table' in data:
            print("\n  Tabela de Diferenças (amostra):")
            for i, diff in enumerate(data['table'][:5]):  # Mostra apenas as primeiras 5 ordens
                print(f"    Ordem {i}: {diff[:5]}...")  # Mostra apenas os primeiros 5 elementos