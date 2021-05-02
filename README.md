# API do Modelo de Propensão Revenda

## Steps para execução da API e Web App
### 1. Download

Faça o download ou clone o código na sua máquina local

## 2. Crie um ambiente python com Anaconda
`conda create --name <environment_name> python==3.7.10`

## 3. Instale os pacotes necessários
`python install -r requirements.txt`

## 4. Inicie o serviço da API
`uvicorn api:app --reload`

## 5. Experimente a API
Abra o seguinte caminho no seu navegador:
* `http://127.0.0.1:8000/docs`
* Clique no endpoint `/predict` e depois em `Try it out` 
* Só preencher os valores desejados das features e clicar em `Execute` 

## 6. Executar o Web App
`streamlit run web_app.py`

# Sobre o Projeto
Esse projeto foi feito com a [base de dados pública da Olist disponibilizada no Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

A tabela utilizada para treinar o modelo, também chamada de dataset ou abt (analytical base table) foi criada a partir dos dados transacionais disponibilizados pela Olist. Para replicar o `ETL` reponsável pela criação do dataset de treinamento, realize os seguintes passos:

1. Faça o download das bases da Olist: https://www.kaggle.com/olistbr/brazilian-ecommerce e disponibilize as bases baixadas na pasta `datasets`.
2. Execute o código `notebooks/01_criando_abt.ipynb`. Esse código no final irá criar e disponibilizar a tabela `datasets/propensao_revenda_abt.csv` na pasta `datasets`;
3. Caso queira também realizar o treinamento do modelo, pode executar o notebook em `notebooks/02_model_training.ipynb` que no final irá criar e disponibilizar um modelo em `models/modelo_final.pkl`.

# Tecnologias Utilizadas

1. [Python](https://www.python.org/): linguagem de programação
2. [Anaconda](https://www.anaconda.com/): gerenciamento de ambientes virtuais
3. [Numpy](https://numpy.org/): processamento de dados
4. [Pandas](https://pandas.pydata.org/): processamento de dados
5. [Scikit-learn](https://scikit-learn.org/stable/): machine learning
6. [Pycaret](https://pycaret.org/): machine learning
7. [FastAPI](https://fastapi.tiangolo.com/): construção de APIs
8. [Streamlit](https://streamlit.io/): construção de Web Apps
