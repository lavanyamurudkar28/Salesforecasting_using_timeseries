import streamlit as st 
import numpy as np
import pickle 
import base64


def load_model():
    with open("saved.space.pkl" , 'rb') as file:
        info = pickle.load(file)
    return info

info = load_model()
model = info["model"]  
le_day = info["le_day"]  
le_month = info["le_month"]
le_year = info["le_year"]
le_item = info["le_item"]

def show_predict_page():

   
 
     
     def local_css(file_name):
        with open(file_name) as f:
           st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

     local_css("style.css")
     left,right= st.columns((9,1))
     

     left.title("Sales forecasting")
     
     left.write(' **WE NEED SOME INFORMATION TO PREDICT SALES** ')

     day = (
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31"

     )

     month = (
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12"
     )

     year = (
        "2013",
        "2014",
        "2015",
        "2016",
        "2017",
        "2018"
          
     ) 

     item =( 
        "1",
        "2",
         "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10"
       
       
     )

     item = left.selectbox("**ITEM**" , item)
     year = left.selectbox("**YEAR** ", year)
     month = left.selectbox("**MONTH** ", month)
     day = left.selectbox("**DAY**" , day)
    
    
    
     ok = left.button("Calculate Sales")
     if ok:
        day = float(day)
        month = float(month)
        year = float(year)
        item = float(item)
        L = np.array([[ day , month, year , item]],dtype = 'float') 
   
        sales = model.predict(L)
        left.subheader(f"the estimated sales are ${sales}")


