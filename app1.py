import pandas as pd
import pickle
import streamlit as st
from PIL import Image
import base64
import io


# Your Streamlit app code goes here

st.set_page_config(
    page_title="Airline App",
    page_icon=":aeroplane:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    f'''
    <style>
    body {{
        background-image: url('C:/Users/AMRITANSHU BATHRE/Downloads/airline satisfaction/airlineimg.jpg');
        background-size: cover;
    }}
    </style>
    ''',
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>MADHAV INSTITUTE OF TECHNOLOGY AND SCIENCE, GWALIOR</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>AIRLINE SATISFACTION PREDICTOR</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> Department of Engineering Mathematics & Computing</h2>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align: center;'>Minor project-02</h2>", unsafe_allow_html=True)


gender=['Male', 'Female']
classes=['Eco Plus', 'Business', 'Eco']
rating=[3, 2, 4, 1, 5, 0]

#import model
pipe=pickle.load(open('pipe1.pkl','rb'))

col1,col2=st.columns(2)
with col1:
    gen_der=st.selectbox('select your gender',gender)
with col2:
    clas=st.selectbox('select your class',classes)

p_age=st.number_input('Age',min_value=0, max_value=100)
dist=st.number_input('Inflight Distance')
delay=st.number_input('Total delay')

col3,col4,col5=st.columns(3)
with col3:
    Wifi_rating=st.selectbox('enter Wifi rating',sorted(rating))
with col4:
    Dep_convenience=st.selectbox('enter Departure/Arrival time convenient',sorted(rating))
with col5:
    booking=st.selectbox('Ease of online Booking',sorted(rating))

col6,col7,col8=st.columns(3)
with col6:
    gate=st.selectbox('Gate Location convenience',sorted(rating))
with col7:
    food_convenience=st.selectbox('Food and drink convenience',sorted(rating))
with col8:
    boarding=st.selectbox('Ease of boarding',sorted(rating))


col9,col10,col11=st.columns(3)
with col9:
    Seat=st.selectbox('Seat Comfort convenience',sorted(rating))
with col10:
    entertainment=st.selectbox('Inflight entertainment',sorted(rating))
with col11:
    On_board_service=st.selectbox('On-board service',sorted(rating))

col12,col13,col14=st.columns(3)
with col12:
    Leg=st.selectbox('Leg room service convenience',sorted(rating))
with col13:
    Baggage=st.selectbox('Baggage handling',sorted(rating))
with col14:
    Checkin=st.selectbox('Checkin service',sorted(rating))

col15,col16=st.columns(2)
with col15:
    Inflight_service=st.selectbox('Inflight service',sorted(rating))
with col16:
    Cleanliness=st.selectbox('Cleanliness',sorted(rating))


if st.button('Predict satisfaction'):
    pass



input_df=pd.DataFrame({'Gender':[gen_der],'Age':[p_age],'Class':[clas],'Flight Distance':[dist],'Inflight wifi service':[Wifi_rating],'Departure/Arrival time convenient':[Dep_convenience],
              'Ease of Online booking':[booking],'Gate location':[gate],'Food and drink':[food_convenience],'Online boarding':[boarding],
              'Seat comfort':[Seat],'Inflight entertainment':[entertainment],'On-board service':[On_board_service],'Leg room service':[Leg],'Baggage handling':[Baggage],
               'Checkin service':[Checkin],'Inflight service':[Inflight_service],'Cleanliness':[Cleanliness],'total delay':[delay]})




st.table(input_df)
st.header('Result is :')
result=pipe.predict_proba(input_df)
st.header(result)
st.header(pipe.predict(input_df))


