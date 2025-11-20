# Global Solution - A Curva do Conhecimento

Este projeto contém a resolução da Global Solution de Differentiated Problem Solving (DPS), que aplica conceitos de Cálculo para modelar a curva de aprendizado.

## Conteúdo da Pasta

- `GS - DPS - Turmas Fevereiro.pdf`: O documento original com as especificações e requisitos do trabalho.

- `trabalho.html`: O relatório final em formato HTML, contendo toda a análise matemática, os gráficos e a conclusão. Este é o principal entregável.

- `gerar_graficos.py`: O script em Python utilizado para gerar os gráficos da curva de conhecimento e da velocidade de aprendizado.

- `requirements.txt`: Um arquivo de texto que lista as bibliotecas Python necessárias para executar o script `gerar_graficos.py`.

- `curva_conhecimento.png`: Imagem do gráfico da curva de conhecimento, utilizada no relatório.

- `velocidade_aprendizado.png`: Imagem do gráfico da velocidade do aprendizado, utilizada no relatório.

## Como Executar (Opcional)

Caso queira recriar os gráficos, você pode seguir estes passos em um terminal:

1.  Crie um ambiente virtual:
    `python3 -m venv .venv`

2.  Ative o ambiente:
    `source .venv/bin/activate`

3.  Instale as dependências:
    `pip install -r requirements.txt`

4.  Execute o script:
    `python gerar_graficos.py`
