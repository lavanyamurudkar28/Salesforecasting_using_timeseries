import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def trending() :
    def local_css(file_name):
        with open(file_name) as f:
           st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("explore.css")
    left,right= st.columns((9,1))
    
    left.title("OVERALL TREND IN DATASET")

    
    train = pd.read_csv("train.csv")
    train_df = train[train['store']==1]
    train_df = train[train['item']==1]
    from statsmodels.tsa.seasonal import seasonal_decompose
    result = seasonal_decompose(train_df['sales'], model='additive', period=365)

    fig = plt.figure()  
    fig = result.plot()  
    fig.set_size_inches(15, 12)

    left.write(fig)