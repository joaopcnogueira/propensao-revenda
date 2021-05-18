# Sobre o Projeto
Esse projeto foi feito com a [base de dados pública da Olist disponibilizada no Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

O objetivo do modelo de machine learning é calcular a propensão de que um dado seller da Olist não irá revender nos próximos 6 meses.

# API e Web App

Foram desenvolvidos diversos tutoriais para executar a API e Web app.

* [Tutorial para execução API e Web App localmente no Windows 10 com Anaconda](tutoriais/tutorial-execucao-api-webapp-windows-10-anaconda.md)
* [Tutorial para execução API e Web App localmente no Windows 10 com Python](tutoriais/tutorial-execucao-api-webapp-windows-10-python.md)
* [Tutorial para execução API e Web App na GCP - Google Cloud Plataform](tutoriais/tutorial-execucao-api-webapp-gcp.md)
* [Tutorial para execução API e Web App na AWS - Amazon Web Service](tutoriais/tutorial-execucao-api-webapp-aws.md)


# Tecnologias Utilizadas



1. [Python](https://www.python.org/): linguagem de programação
2. [Colab](https://colab.research.google.com/notebooks/intro.ipynb): ambiente de treinamento de modelos
3. [Anaconda](https://www.anaconda.com/): gerenciamento de ambientes virtuais
4. [Numpy](https://numpy.org/): processamento de dados
5. [Pandas](https://pandas.pydata.org/): processamento de dados
6. [Scikit-learn](https://scikit-learn.org/stable/): machine learning
7. [Pycaret](https://pycaret.org/): machine learning
8. [FastAPI](https://fastapi.tiangolo.com/): construção de APIs
9. [Streamlit](https://streamlit.io/): construção de Web Apps
10. [Git](https://git-scm.com/): versionamento de código
11. [Github](https://github.com/): repositório de código



# Steps para criação da analytical base table e treinamento do modelo (OPCIONAL)



A tabela utilizada para treinar o modelo, também chamada de dataset ou abt (analytical base table) foi criada a partir dos dados transacionais disponibilizados pela Olist. Para replicar o `ETL` reponsável pela criação do dataset de treinamento, realize os seguintes passos:

1. Faça o download das bases da Olist: https://www.kaggle.com/olistbr/brazilian-ecommerce e disponibilize as bases baixadas na pasta `datasets`.
2. Execute o código `notebooks/01_criando_abt.ipynb`. Esse código no final irá criar e disponibilizar a tabela `datasets/propensao_revenda_abt.csv` na pasta `datasets`;
3. Caso queira também realizar o treinamento do modelo, pode executar o notebook em `notebooks/02_model_training.ipynb` que no final irá criar e disponibilizar um modelo em `models/modelo_final.pkl`.
A tabela utilizada para treinar o modelo, também chamada de dataset ou abt (analytical base table) foi criada a partir dos dados transacionais disponibilizados pela Olist. Para replicar o `ETL` reponsável pela criação do dataset de treinamento, realize os seguintes passos:

1. Faça o download das bases da Olist: https://www.kaggle.com/olistbr/brazilian-ecommerce e disponibilize as bases baixadas na pasta `datasets`.
2. Execute o código `notebooks/01_criando_abt.ipynb`. Esse código no final irá criar e disponibilizar a tabela `datasets/propensao_revenda_abt.csv` na pasta `datasets`;
3. Caso queira também realizar o treinamento do modelo, pode executar o notebook em `notebooks/02_model_training.ipynb` que no final irá criar e disponibilizar um modelo em `models/modelo_final.pkl`.


