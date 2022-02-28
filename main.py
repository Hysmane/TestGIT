import streamlit as st


st.write(" Hello  word ! Stop the war")
st.sidebar.selectbox('select',[6,7,8,9,10,11,12,13,14,15])
input_text= st.text_input('Your name')
input_text
num_input = st.number_input('put any number')
num_input
st.file_uploader('FILE UPLOAD')
st.select_slider( 'A Slider',[10,20,30,40,50,60,70,80,90,100])