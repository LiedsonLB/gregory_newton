import numpy as np

def ler_arquivo(nome_arquivo):
    try:
        data = np.loadtxt(nome_arquivo)
        if data.shape[1] != 2:
            raise ValueError("Arquivo deve conter exatamente 2 colunas")
        # printa os dados lidos
        print(f"Dados lidos do arquivo '{nome_arquivo}':\n{data}")
        return data[:, 0], data[:, 1]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado")
    except Exception as e:
        raise ValueError(f"Erro ao ler arquivo: {str(e)}")

def formatar_dados(dados):
    return [(x, y) for x, y in zip(dados[0], dados[1])]