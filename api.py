import numpy as np
import pandas as pd
from fastapi import FastAPI
from pycaret.classification import load_model, predict_model

# criando o app da nossa API
app = FastAPI()

# carregando o modelo
model = load_model('models/modelo_final')

# endpoint inicial
@app.get('/')
def hello():
    return "Bem-vindo a API de previsão de revenda!"

# endpoint predict
@app.post('/predict/')
def predict(uf: str, 
            tot_orders_12m: int, 
            tot_items_12m: int, 
            tot_items_dist_12m: int, 
            receita_12m: float, 
            recencia: int):

    df_new = pd.DataFrame([[uf, tot_orders_12m, tot_items_12m, tot_items_dist_12m, receita_12m, recencia]])
    df_new.columns = ['uf', 'tot_orders_12m', 'tot_items_12m', 'tot_items_dist_12m', 'receita_12m', 'recencia']

    predictions = predict_model(model, data=df_new)
    predictions['proba_nao_revender_next_6m'] = np.where(predictions['Label'] == 1, predictions['Score'], 1-predictions['Score'])
    return {"proba_nao_revender_next_6m": predictions['proba_nao_revender_next_6m'][0]}
