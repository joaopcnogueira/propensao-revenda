import numpy as np
import pandas as pd
import base64
import streamlit as st
from pycaret.classification import load_model, predict_model

model = load_model('models/modelo_final')

def run():

    add_selectbox = st.sidebar.selectbox("Como você gostaria de fazer a sua predição?", ("Online", "Batch"))
    
    st.title("Previsão de Não Revenda")

    if add_selectbox == 'Online':

        uf = st.selectbox('UF', ['SP', 'ES','GO','PR','MG','RN','SC','RJ','RS','PB','DF','PE','MT','AM','RO','CE','BA','SE','MS','PA'])
        tot_orders_12m = st.number_input('Total de Pedidos', min_value=0, max_value=1000, value=5)
        tot_items_12m = st.number_input('Total de Items', min_value=0, max_value=1000, value=5)
        tot_items_dist_12m = st.number_input('Total de Items Distintos', min_value=0, max_value=1000, value=5)
        receita_12m = st.number_input('Receita', min_value=0, max_value=1000000, value=5)
        recencia = st.number_input('Recência', min_value=0, max_value=1000, value=5)

        
        input_dict = {'uf' : uf, 
                      'tot_orders_12m' : tot_orders_12m, 
                      'tot_items_12m' : tot_items_12m, 
                      'tot_items_dist_12m' : tot_items_dist_12m, 
                      'receita_12m' : receita_12m, 
                      'recencia' : recencia}
        input_df = pd.DataFrame([input_dict])
        
        if st.button("Predict"):
            predictions = predict_model(estimator=model, data=input_df)
            predictions['proba_nao_revender_next_6m'] = np.where(predictions['Label'] == 1, predictions['Score'], 1-predictions['Score'])
            score = float(predictions['proba_nao_revender_next_6m'].values[0])
            st.success(f'A probabilidade do seller não revender nos próximos 6 meses é de {score:.2f}')

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model, data=data)
            predictions['proba_nao_revender_next_6m'] = np.where(predictions['Label'] == 1, predictions['Score'], 1-predictions['Score'])
            # mostra a tabela com as previsões no site
            st.write(predictions)
            # cria o link de download da tabela com as previsões
            csv = predictions.to_csv(sep=';', index=False)
            b64 = base64.b64encode(csv.encode()).decode() # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == '__main__':
    run()
