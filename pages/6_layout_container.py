import streamlit as st
import numpy as np

st.header('Column layout')

col=st.columns(3)
col[0].subheader('영역1')
col[0].image('https://static.streamlit.io/examples/cat.jpg')

col[1].subheader('영역2')
col[1].image('https://static.streamlit.io/examples/dog.jpg')

col[2].subheader('영역3')
col[2].image('https://static.streamlit.io/examples/owl.jpg')

st.divider()

col1,col2,col3=st.columns(3)
col1.subheader('영역1')
col1.image('https://static.streamlit.io/examples/cat.jpg')

col2.subheader('영역2')
col2.image('https://static.streamlit.io/examples/dog.jpg')

col3.subheader('영역3')
col3.image('https://static.streamlit.io/examples/owl.jpg')

st.divider()

col1,col2,col3=st.columns(3)
with col1:
    st.subheader('영역1')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2:
    st.subheader('영역2')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3:
    st.subheader('영역3')
    st.image('https://static.streamlit.io/examples/owl.jpg')

st.divider()

col1,col2=st.columns([1,3]) # 전체 영역을 1:3의 비율로 나누는 것(2개로 나눔)
data=np.random.randn(10,1)

with col1:

    st.metric('점수',55,0.5)

with col2:
    st.line_chart(data)

col1,col2,col3=st.columns([1,2,2])
data=np.random.randn(10,1)

with col1:

    st.metric('점수',55,0.5)

with col2:
    st.line_chart(data)

with col3:
    st.bar_chart(data)

col1,col2,col3=st.columns([1,2,2],gap='medium')
data2=np.random.randn(10,1)

with col1:

    st.metric('점수',55,0.5)

with col2:
    st.line_chart(data2)

with col3:
    st.bar_chart(data2)


st.divider()

st.header('Container')

with st.container(border=True):
    st.write('컨테이너 내부')
    st.bar_chart(np.random.randn(50))
st.write('컨테이너 외부')

st.subheader('2. 컨테이너에 요소 추가')
container=st.container(border=True)
container.write('컨테이너 안에 있어요')
container.area_chart(data)
st.write('컨테이너외부에있어요')
container.button('시작') # 컨테이너 안으로 들어감

st.divider()

st.subheader('3. 그리드모양의 컨테이너 구성')

row1=st.columns(3)
row2=st.columns(3)

for col in row1+row2:
    tile=col.container(height=120)
    tile.subheader(':smile:')

st.divider()

with st.container(height=300):
    st.markdown('long_text '*300)

import time


st.divider()
st.header('Empty container: single element``')
with st.empty():
    for seconds in range(4):
        st.write(f'{seconds}초')
        time.sleep(1)
    st.write('time over')

    # st.write('first')
    # st.write('second')
    # st.write('third')

empty=st.empty()
empty.text('Hello')
empty.line_chart(data)