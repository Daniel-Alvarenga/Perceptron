# Perceptron

## Introdução

O **Perceptron** é um neurônio artificial simples que simula o comportamento de um neurônio biológico. Ele pode ser usado para resolver problemas de classificação binária. Esta documentação fornece uma visão geral do que é um Perceptron, como ele é treinado e quais dados são plotados durante o treinamento.

## O que é um Perceptron?
![neuronio-1](https://github.com/Daniel-Alvarenga/Perceptron/assets/128755697/5cfe9ba3-1fe3-4e4b-96d0-4e88d89cc1a0)

Um Perceptron é um bloco básico das redes neurais artificiais. Ele recebe um conjunto de valores de entrada, aplica pesos a essas entradas, soma-os e, em seguida, passa o resultado por uma função de ativação para produzir uma saída. A saída é usada para tomar decisões binárias, como classificar dados em duas categorias.

## Treinando um Perceptron

O treinamento de um Perceptron envolve ajustar seus pesos e viés para aprender o limite de decisão apropriado para os dados fornecidos. Isso é tipicamente feito usando um processo de aprendizado supervisionado. Durante o treinamento, o Perceptron atualiza iterativamente seus pesos e viés com base no erro entre as saídas previstas e os alvos reais.

## Dados Plotados

Durante o processo de treinamento, os seguintes dados são plotados para visualizar o progresso da aprendizagem:
- Variação de `w1`, `w2`, `bias`, `dbias`, `dw1` e `dw2` ao longo do tempo.

## Uso

Siga estas etapas para usar o Perceptron:

### Pré-requisitos

1. Certifique-se de ter o Python 3.x instalado em seu sistema.

### Configurando um Ambiente Virtual (Opcional, mas Recomendado)

1. Crie um ambiente virtual (venv) para isolar as dependências:
python -m venv ambiente-perceptron


2. Ative o ambiente virtual:
- No Windows:
  ```
  .\ambiente-perceptron\Scripts\activate
  ```
- No macOS e Linux:
  ```
  source ambiente-perceptron/bin/activate
  ```

### Instalando Dependências

1. Clone ou baixe este repositório.
git clone https://github.com/Daniel-Alvarenga/Perceptron


3. Navegue até o diretório do repositório:
cd caminho/para/pasta-do-perceptron


4. Instale as dependências necessárias usando o pip e o arquivo `requirements.txt`:
pip install -r requirements.txt


### Executando o Perceptron

1. Execute o script do Perceptron:
python perceptron.py


2. Siga as instruções na tela para testar e treinar o Perceptron.

### Desativando o Ambiente Virtual

Se você usou um ambiente virtual, desative-o quando terminar:
deactivate


## Conclusão

O Perceptron é um conceito fundamental em redes neurais e pode ser uma ferramenta poderosa para resolver problemas de classificação binária. Esta documentação fornece uma introdução ao Perceptron, seu processo de treinamento e os dados que são visualizados durante o treinamento. Siga as instruções fornecidas para configurar e usar o Perceptron em seus próprios projetos.
