import streamlit as st

with st.sidebar:
    st.radio('학년', ('1학년', '2학년'))

choice = st.sidebar.selectbox('학년', ('1학년', '2학년'))
st.write(choice)

with st.sidebar:
    st.page_link('pages/1_Text_elements.py', label='1_Text_elements.py')
    st.page_link('https://www.google.com', 'google')
    st.page_link('https://www.naver.com', 'naver')

