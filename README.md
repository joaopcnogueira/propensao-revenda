# Sobre o Projeto
Esse projeto foi feito com a [base de dados pública da Olist disponibilizada no Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

O objetivo do modelo de machine learning é calcular a propensão de que um dado seller da Olist não irá revender nos próximos 6 meses.

A tabela utilizada para treinar o modelo, também chamada de dataset ou abt (analytical base table) foi criada a partir dos dados transacionais disponibilizados pela Olist. Para replicar o `ETL` reponsável pela criação do dataset de treinamento, realize os seguintes passos:

1. Faça o download das bases da Olist: https://www.kaggle.com/olistbr/brazilian-ecommerce e disponibilize as bases baixadas na pasta `datasets`.
2. Execute o código `notebooks/01_criando_abt.ipynb`. Esse código no final irá criar e disponibilizar a tabela `datasets/propensao_revenda_abt.csv` na pasta `datasets`;
3. Caso queira também realizar o treinamento do modelo, pode executar o notebook em `notebooks/02_model_training.ipynb` que no final irá criar e disponibilizar um modelo em `models/modelo_final.pkl`.

# API e Web App

## Steps para execução da API e Web App
### 1. Instale o Git
* Link para download: https://git-scm.com/downloads

### 2. Faça o clone do código fonte
Abra o `CMD` e digite o seguinte comando para baixar o código

`git clone https://github.com/joaopcnogueira/propensao-revenda.git`

Depois de finalizado, digite o comando `dir` e verifique que uma pasta chamada `propensao-revenda` agora existe no seu computador.
Essa pasta contém todo o código fonte da nossa aplicação.

### 3. Instale o Anaconda
* Link para download: https://www.anaconda.com/products/individual

## 4. Crie um ambiente python com Anaconda
`conda create --name <environment_name> python==3.7.10`

## 5. Instale os pacotes necessários
`pip install -r requirements.txt`

## 6. Inicie o serviço da API
`uvicorn api:app --reload`

## 7. Experimente a API
Abra o seguinte caminho no seu navegador:
* `http://127.0.0.1:8000/docs`
* Clique no endpoint `/predict` e depois em `Try it out` 
* Só preencher os valores desejados das features e clicar em `Execute` 

## 8. Executar o Web App
`streamlit run web_app.py`

# Tecnologias Utilizadas

1. [Python](https://www.python.org/): linguagem de programação
2. [Anaconda](https://www.anaconda.com/): gerenciamento de ambientes virtuais
3. [Numpy](https://numpy.org/): processamento de dados
4. [Pandas](https://pandas.pydata.org/): processamento de dados
5. [Scikit-learn](https://scikit-learn.org/stable/): machine learning
6. [Pycaret](https://pycaret.org/): machine learning
7. [FastAPI](https://fastapi.tiangolo.com/): construção de APIs
8. [Streamlit](https://streamlit.io/): construção de Web Apps
