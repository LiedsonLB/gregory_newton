def show_main_menu():
    """
    Exibe o menu principal e obtém a escolha do usuário
    """
    print("\nMenu Principal:")
    print("1. Testar com dados de arquivo")
    print("2. Testar com dados gerados")
    print("3. Análise de desempenho")
    print("4. Sair")
    return input("Escolha uma opção: ")

def get_interpolation_point():
    """
    Obtém o ponto para interpolar do usuário
    """
    return float(input("\nDigite o valor de x para interpolar: "))

def get_data_parameters():
    """
    Obtém parâmetros para geração de dados
    """
    n = int(input("Digite o número de pontos a gerar: "))
    spacing = input("Espaçamento (equal/random): ").lower()
    return n, spacing

def get_file_path():
    """
    Obtém caminho do arquivo de dados
    """
    return input("Digite o caminho do arquivo de dados: ")