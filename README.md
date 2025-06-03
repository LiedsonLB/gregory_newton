# Sistema de Análise de Métodos de Interpolação - Gregory-Newton

[![Versão](https://img.shields.io/github/v/release/LiedsonLB/gregory_newton)](https://github.com/LiedsonLB/gregory_newton/releases)
[![Forks](https://img.shields.io/github/forks/LiedsonLB/gregory_newton)](https://github.com/LiedsonLB/gregory_newton/network/members)
[![Contribuidores](https://img.shields.io/github/contributors/LiedsonLB/gregory_newton)](https://github.com/LiedsonLB/gregory_newton/graphs/contributors)
[![Pull Requests Abertos](https://img.shields.io/github/issues-pr/LiedsonLB/gregory_newton)](https://github.com/LiedsonLB/gregory_newton/pulls)
[![Última Atualização](https://img.shields.io/github/last-commit/LiedsonLB/gregory_newton)](https://github.com/LiedsonLB/gregory_newton/commits/master) 

![Banner de Interpolação Numérica](/snapshots/banner_matplotlib.PNG)

## Sobre o Projeto
Este projeto implementa e compara três métodos clássicos de interpolação numérica:

- Gregory-Newton (para pontos igualmente espaçados)
- Lagrange (para qualquer disposição de pontos)
- Newton-Geral (diferenças divididas)

O sistema permite testar os métodos com dados de arquivos ou gerados automaticamente, além de realizar análises de desempenho comparativo.

## Tecnologias Utilizadas

<div style="display: flex; flex-wrap: wrap; gap: 5px; justify-content: center">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" height="30" width="40">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" alt="NumPy" height="30" width="40">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" alt="Matplotlib" height="30" width="40">
</div>

## Métodos Implementados

1. `Gregory-Newton`: Pontos igualmente espaçados
Complexidade: O(n²) construção, O(n) avaliação
Limitação: Requer espaçamento uniforme entre pontos

2. `Lagrange`: Funciona com qualquer disposição de pontos
Complexidade: O(n²) para cada avaliação
Limitação: Computacionalmente ineficiente para muitos pontos

3. `Newton-Geral` (Diferenças Divididas): Precisão e desempenho
Complexidade: O(n²) construção, O(n) avaliação
Vantagem: Fácil adição de novos pontos

## Configuração do Projeto
Pré-requisitos

- Python 3.8+
- Bibliotecas: NumPy, Matplotlib

## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/LiedsonLB/gregory_newton.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o script principal:
```bash
python main.py
```

## Uso

O sistema permite escolher entre três opções de ações:
```python
1. Testar com dados de arquivo
2. Testar com dados gerados
3. Análise de desempenho
4. Sair
```

## Formatos de Entrada
Os dados de entrada podem ser fornecidos em dois formatos:
- **Arquivo TXT**: Com colunas `x` e `y` representando os pontos.
````txt
0.0 1.0
1.0 2.5
2.0 3.5
...
````
- **Gerados Automaticamente**: Especificando o número de pontos e a função a ser interpolada.

# 📊 Saídas
## Resultados Numéricos
- Valor interpolado
- Tabela de diferenças
- Estatísticas de execução

## Visualizações
Gráficos comparativos:
- `Iterações` x `Número de pontos`
- `Operações` x `Número de pontos`

## Limitações
- Overflow numérico com relação a entrada: n > 5.000
- Precisão reduzida em extremos do intervalo
- Gregory-Newton requer espaçamento uniforme

# Autores
- [Maria Clara](https://github.com/clara0904)
- [Kaio Simeão](https://github.com/KaioSimeao)
- [João Marcello](https://github.com/Joaomarcellodev)
- [Francisco Liédson](https://github.com/LiedsonLB)

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

## Releases

- Release v1.0.0 ✅ - [Release v1.0.0](https://github.com/LiedsonLB/gregory_newton/releases/tag/v1.0.0)