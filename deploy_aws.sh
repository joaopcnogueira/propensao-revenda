# -----------------------------------------------------------
# Script para deploy em uma instância da Amazon Web Service
# com sistema operacional ubuntu-20.04
# -----------------------------------------------------------

# Instalar as dependencias no sistema operacional

sudo apt update -y
sudo apt install python3-pip python3-venv -y

DIR_ENV=env_deploy
if [ ! -d "$DIR_ENV" ]
then
echo 
echo "----------------------------------"
echo "Virtualenv NAO EXISTE, criando ..."
echo "----------------------------------"
# Criar ambiente virtual com o Python
python3 -m venv env_deploy
fi

echo 
echo "-------------------------------"
echo "Virtualenv EXISTE, ativando ..."
echo "-------------------------------"
echo
source env_deploy/bin/activate

sleep 5

# Atualizar o pip 
pip install -U pip setuptools

sleep 5

pip install pycaret

deactivate

sleep5

source env_deploy/bin/activate

# Instalar os pacotes necessários
pip install pycaret
sleep 5
pip install fastapi
sleep 5
pip install streamlit
sleep 5
pip install uvicorn uvloop

echo 
echo "-----------------------------------"
echo "Aguardando instalação finalizar ..."
echo "-----------------------------------"
echo
sleep 30

# Executar a api fastapi: http://SEU_IP:8000/docs
uvicorn api:app --host=0.0.0.0 --port=${PORT:-8000} &

sleep 10

# Executar o comando abaixo para o web app: http://SEU_IP:8501
streamlit run web_app.py