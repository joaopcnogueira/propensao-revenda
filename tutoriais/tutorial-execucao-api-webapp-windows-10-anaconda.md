## Tutorial deploy no Windows 10 com Anaconda
### 1. Instale o Git
* Link para download: https://git-scm.com/downloads

![Git Download](./imagens/download_git.png)

### 2. Faça o clone do código fonte
Abra o `CMD` e digite o seguinte comando para baixar o código

```
git clone https://github.com/joaopcnogueira/propensao-revenda.git
```

![Git Clone](./imagens/git_clone.png)

Depois de finalizado, digite o comando `dir` e verifique que uma pasta chamada `propensao-revenda` ou `propensao-revenda-main` agora existe no seu computador.
Essa pasta contém todo o código fonte da nossa aplicação. Navegue até a pasta digitando o seguinte comando no `CMD`

```
cd propensao-venda
```

ou 

```
cd propensao-venda-main
```

### 3. Instale o Anaconda
* Link para download: https://www.anaconda.com/products/individual

No momento da instalação, selecionar a seguinte opção: `Add Anaconda3 to my PATH environment variable`

![Anaconda Path](./imagens/anaconda_instalacao.png)


### 4. Crie um ambiente python com Anaconda

```
conda create --name ambiente_api python==3.7.10
```

### 5. Ative o ambiente python criado no passo anterior

```
conda activate ambiente_api
```

### 6. Instale os pacotes necessários

```
pip install -r requirements.txt
```

Caso o comando acima não funciona, executar o comando abaixo:

```
pip install --user -r requirements.txt
```

### 7. Inicie o serviço da API

```
uvicorn api:app --reload
```

### 8. Experimente a API
Abra o seguinte caminho no seu navegador:
* `http://127.0.0.1:8000/docs`
* Clique no endpoint `/predict` e depois em `Try it out` 
* Só preencher os valores desejados das features e clicar em `Execute` 

### 9. Para executar o Web App, abra outro `CMD` dentro do diretório que estão os códigos e execute os comandos abaixo

```
conda activate ambiente_api # ativar o ambiente python
streamlit run web_app.py # executando o streamlit
```

### 10. Abra a página do web app digitando o endereço abaixo no navegador

```
http://127.0.0.1:8501
```

