import streamlit as st
import pandas as pd

##Main Function
def anonymise_categorical_variable(DATAFRAME, COLS):
    
    for col in COLS:
        anom = []
        res_dict = {}
        ind = DATAFRAME[col].unique()
        
        for i in range(len(ind)):
            anom.append(col+"_"+str(i))
        
        for k, v in zip(ind, anom):
            res_dict.update({k:v})        
        
        #DATAFRAME[col+'_'+'Anonym'] = DATAFRAME[col].map(res_dict)
        DATAFRAME[col] = DATAFRAME[col].map(res_dict)
        #pd.rename({col:col+'_'+'Anonym'}, axis=1, inplace=True)

    st.write("Output Dataset:")
    #st.dataframe(df.drop(columns=DIFF))

st.header("The Anonymizer")
st.markdown("Replace any sensitive **categorical** feature in a dataset, for example, if you have the countries AUS, COL, ARG these are replaced by Country_1, Country_2, Country 3")
st.markdown("Developed by: **Jhonnatan Torres**")
data = st.file_uploader("Upload a csv file", type=["csv"])

if data is not None:
    df = pd.read_csv(data)
    CAT_COLS = df.select_dtypes(include=['object']).columns.tolist()
    TO_REMOVE = st.multiselect("Columns to remove from process:", df.columns)     
    DIFF = list(set(CAT_COLS)-set(TO_REMOVE))
    st.write("Columns included in the process: ",str(DIFF))
    st.write("Input Dataset:")
    st.dataframe(df)

    anonymise_categorical_variable(DATAFRAME=df, COLS=DIFF)
    st.download_button(label="Download Data", data=df.to_csv().encode('utf-8'), file_name='df_anonym.csv')