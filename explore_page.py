import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px




    
def show_explore_page():
    def local_css(file_name):
        with open(file_name) as f:
           st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("explore.css")
    left,right= st.columns((9,1))
    
    left.title("Explore sales analysis")
    left.write("""sales with respect to date""")
    
    train = pd.read_csv("train.csv")
    train_df = train[train['store']==1]
    train_df = train_df[train['item']==1]
   
   
    fig =px.line(train_df,x="date",y="sales",width = 1000, height=400)
  
   
    left.write(fig)
    

   


    
    

