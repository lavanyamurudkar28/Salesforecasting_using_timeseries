import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def pie():
    def local_css(file_name):
        with open(file_name) as f:
           st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("explore.css")
    left,right= st.columns((9,1))
    
    left.title("Pie CHART")
    left.write("""sales with respect to items""")
    
    train = pd.read_csv("train.csv")
    train_df = train[train['store']==1]
    train_df = train[train['item']<=10]
   
   
    eig =px.pie(train_df,values ='sales',names='item')
  
   
    left.write(eig)
    
    
    

