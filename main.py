import numpy as np
from methods.gregory_newton import gregory_newton_interpolation
from methods.lagrange import lagrange_interpolation
from methods.newton_geral import newton_general_interpolation
from utils.data_loader import ler_arquivo  
from utils.data_generator import generate_test_data
from utils.performance import compare_methods, performance_analysis
from interface.menu import (show_main_menu, get_interpolation_point, 
                          get_data_parameters, get_file_path)
from interface.results import print_results

def main():
    print("Sistema de Análise de Métodos de Interpolação")
    
    while True:
        choice = show_main_menu()
        
        if choice == '1':  # Dados de arquivo
            try:
                filename = get_file_path()
                x, y = ler_arquivo(filename)
                print("\nDados carregados com sucesso!")
                xi = get_interpolation_point()
                results = compare_methods(x, y, xi)
                print_results(results)
            except Exception as e:
                print(f"\nErro: {str(e)}")
        
        elif choice == '2':  # Dados gerados
            try:
                n, spacing = get_data_parameters()
                x, y = generate_test_data(n, spacing)
                print("\nDados gerados com sucesso!")
                print(f"Dados gerados: x = {x}, y = {y}")
                xi = get_interpolation_point()
                results = compare_methods(x, y, xi)
                print_results(results)
            except Exception as e:
                print(f"\nErro: {str(e)}")
        
        elif choice == '3':  # Análise de desempenho
            try:
                max_points = int(input("\nNúmero máximo de pontos para análise: "))
                performance_analysis(max_points)
            except Exception as e:
                print(f"\nErro: {str(e)}")
        
        elif choice == '4':  # Sair
            print("\nEncerrando o programa...")
            break
        
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()