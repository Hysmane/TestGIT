import streamlit as st


st.write(" Hello  World !! Stop the War")
st.sidebar.selectbox('select',[6,7,8,9,10,11,12,13,14,15])
input_text= st.text_input('Your name')
input_text
num_input = st.number_input('put any number')
num_input
st.file_uploader('FILE UPLOAD')
st.select_slider( 'A Slider',[10,20,30,40,50,60,70,80,90,100])
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/syousmanesy@yahoo.fr" method ="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()