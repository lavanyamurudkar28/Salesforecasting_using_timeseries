import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

from residue import trending
from pie import pie
import base64

def set_bg_hack(main_bg):
    
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack('background.png')


page = st.sidebar.selectbox("Explore or predict", ("predict", "Explore","trend","pie_chart"))



if page ==  "predict":
    show_predict_page()
    
    
elif page == "Explore":
    show_explore_page()

elif page == "trend":
    trending()

else  :
    pie()
    
