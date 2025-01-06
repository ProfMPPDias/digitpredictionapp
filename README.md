# Aplicação de Previsão de Dígitos Desenhados com Machine Learning

Este projeto utiliza a biblioteca `tkinter` para criar uma interface gráfica onde o usuário pode desenhar um dígito, e um modelo de Machine Learning (Random Forest) é usado para prever o número desenhado. O modelo foi treinado com o conjunto de dados MNIST.

## Funcionalidades

- Interface gráfica onde o usuário pode desenhar um número.
- O número desenhado é previsto por um modelo de classificação de dígitos.
- O modelo de Machine Learning é treinado utilizando o conjunto de dados MNIST.
- Exibe a previsão do número desenhado com a atualização de LEDs na interface.

## Requisitos

Antes de executar o projeto, instale as dependências necessárias:

### 1. Instalar o Python (caso ainda não tenha):
Certifique-se de ter o Python 3.7 ou superior instalado. Você pode baixar o Python a partir do [site oficial](https://www.python.org/downloads/).

### 2. Instalar dependências:

Para instalar as dependências necessárias, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

### 3. Conteúdo do arquivo requirements.txt:

```bash
tkinter
scikit-learn
numpy
matplotlib
Pillow
```

### Como usar:

1. Clone o repositório.
```bash
git clone https://github.com/ProfMPPDias/digitpredictionapp.git
```
3. Navegue até a pasta do projeto no terminal.
```bash
cd digitpredictionapp
```
5. Execute o script Python:
```bash
python main.py
```
4. A janela da aplicação será aberta. Desenhe um número no painel e clique no botão "Prever" para ver a previsão do número desenhado.

## Estrutura do código

#Função Principal:

O modelo é treinado com o conjunto de dados MNIST utilizando o RandomForestClassifier da biblioteca scikit-learn.
A interface gráfica permite que o usuário desenhe um número. O desenho é processado, e o número previsto é exibido na tela.
A previsão é feita utilizando a função predict_digit.

##Bibliotecas usadas:

- tkinter: para a criação da interface gráfica.
- Pillow: para processar as imagens desenhadas.
- scikit-learn: para treinamento e predição do modelo de Machine Learning.
- matplotlib: para visualização (não é usado diretamente neste script, mas pode ser útil para análise adicional).

##Contribuição

Sinta-se à vontade para fazer melhorias no código ou criar novos recursos. Caso deseje contribuir, siga os passos abaixo:

- Fork o repositório.
- Crie uma nova branch.
- Faça as suas mudanças.
- Submeta um pull request.
