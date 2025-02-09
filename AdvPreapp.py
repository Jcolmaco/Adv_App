import streamlit as st
import pickle 
import pandas as pd

st.title('Advertising Sales Predictor App')
st.write('This web application estimates the revenue from an advertising campaign by analyzing the budgets allocated to TV, Radio, and Newspaper.')

with open('model_Advertising_model', 'rb') as file:
    model_cp = pickle.load(file)


st.write('Enter your budget (in $1,000s)')
tv_value=st.number_input('**TV Advertising Budget:**')
radio_value=st.number_input('**Radio Advertising Budget:**')
newspaper_value=st.number_input('**Newspaper Advertising Budget:**')


ad_data=pd.DataFrame({'TV':tv_value, 'Radio':radio_value, 'Newspaper':newspaper_value},index=[0])


prediction=model_cp.predict(ad_data)


if st.button('Predict'):
    formatted_prediction = f"${prediction[0]:,.2f}"
    st.write(f'The predicted sales value is {formatted_prediction}')


