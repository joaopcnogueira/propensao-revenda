# API do Modelo de Propensão a Não Revender

## Steps
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
