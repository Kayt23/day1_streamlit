import streamlit as st
import datetime

st.title("Form for Blood Donors")
st.write("Please answer some questions before your blood donation")

user_id = st.text_input("Name",value="Your Name", max_chars=30)
info = st.text_area("Share some information about you", "Put information here",help='You should write about what kind of disease you have or medicine you are allergic to ')
blood_type = st.text_input("Blood type",value="Your blood type")
age = st.number_input("Age",min_value=18,max_value=100,step=1)
birth_date = st.date_input("Date of Birth",min_value=datetime.date(1921,1,1),max_value=datetime.date(2003,12,31))
last_donation= st.date_input("Last time you donated blood",min_value=datetime.date(1999,12,31),max_value=datetime.date(2021,9,19))
smoke = st.checkbox("Do you smoke?")
weight = st.slider("Choose your weight",min_value=99.,max_value=150.,step=.5)
sleep = st.selectbox("Select your sleeping hours last night",options=["6","7","8","9"])
physical_form = st.selectbox("Select level of your physical condition",options=["Normal","Good","Bad"])
food_intake = st.selectbox("Have you had your breakfast?",options=["Yes","No"])

image = st.file_uploader("Take your photo and upload it",type=['jpg','png'])
st.write("After donation,we would like to give you a gift as a token of appreciation.")
gift=st.multiselect('Please choose two you would like to recieve.',options=['book','bag','snacks','ballpen','glass'])

submit=st.button("Submit")
if submit:
    st.write("You have submitted the form.")

