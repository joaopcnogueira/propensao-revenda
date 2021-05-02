# ------------------------------------------------------------
# Script para deploy em uma instância do Google Compute Engine
# com sistema operacional ubuntu-20.04
# ------------------------------------------------------------

# clonar o rojeto na instância (servidor)
git clone https://github.com/joaopcnogueira/propensao-revenda.git

# baixar o miniconda (pacote menor que o anaconda para agilizar o deploy)
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh

# instalar miniconda
bash Miniconda3-py39_4.9.2-Linux-x86_64.sh

# reativar o arquivo .bashrc para que o shell já reconheça o miniconda
source .bashrc

# criar ambiente virtual do python com miniconda
conda create --name deploy python==3.7.10

# ativar o ambiente virtual
conda activate deploy

# navegar até a pasta com os códigos
cd propensao-revenda

# instalar os pacotes
pip install -r requirements.txt

# executar a api fastapi: http://SEU_IP:8000/docs
uvicorn api:app --host=0.0.0.0 --port=${PORT:-8000}

# abrir outro ssh, e executar o comando abaixo para o web app: http://SEU_IP:8501
streamlit run web_app.py
