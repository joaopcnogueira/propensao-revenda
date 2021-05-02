# clonando o projeto
sudo apt-get update
sudo apt-get install git-all
git clone https://github.com/joaopcnogueira/propensao-revenda.git

# instalando o anaconda
sudo apt-get install wget
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh
bash Miniconda3-py39_4.9.2-Linux-x86_64.sh # fechar e abrir outro shell depois de finalizando a instalação

# criando e ativando o ambiente virtual
conda create --name deploy python==3.7.10
conda activate deploy

# instalando as dependências
cd propensao-revenda
pip install -r requirements.txt

# executar o servidor fastapi
uvicorn api:app --reload