import streamlit as st

st.title('Input Widgets!')
st.header('1. Button elements')
st.subheader('Button')
st.button('초기화', type='primary')
if st.button('안녕'):
    st.write('반가워:smile:')
else:
    st.write('잘가!:raising_hand:')

st.subheader('Link Button', divider=True)
st.link_button('google','https://www.google.com')

st.subheader('Page Link')
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/1_Text_elements.py", label="Text elements", icon="1️⃣")
st.page_link("pages/2_Data_elements.py", label="Data elements", icon="2️⃣")
st.page_link("pages/박병호_streamlit_연습문제.py", label="Exercise", disabled=True)
st.page_link("https://docs.streamlit.io/develop/api-reference/widgets/st.page_link", label="Streamlit Docs", icon="🌎")
# st.page_link("http://www.google.com", label="Google", icon="🌎")

st.subheader('Submit', divider=True)

with st.form(key='form1'):
    id=st.text_input('Id')
    pw=st.text_input('Password', type='password')
    submitted=st.form_submit_button()
    if submitted:
        st.write('Id:', id, 'password:', pw)

form=st.form(key='form2')
title=form.text_input('제목')
contents=form.text_area(('질문입력'))
submit=form.form_submit_button('작성')
if submit:
    st.write('제목:',title,'이(가) 등록되었습니다')


st.divider()
st.header('2. Selection elements')
st.subheader('Checkbox')

agree=st.checkbox('찬성', value=True, label_visibility='visible')
if agree:
    st.write('Good!')

# agree=st.checkbox('찬성', value=True, label_visibility='hidden')
# if agree:
#     st.write('Good!')

st.subheader('Toggle',divider=True)
on=st.toggle('선택')
if on:
    st.write('on')

st.subheader('Radio',divider=True)
fruit=st.radio(
    '좋아하는 과일은?',
    [':banana:바나나','딸기','메론','사과','배'],
    captions=['웃어요','달콤해요','시원해요','상큼해요','즙이 많아요'],
    horizontal=True,
)
if fruit==':banana:바나나':
    st.write('바나나를 선택했군요')
else:
    st.write('바나나를 선택하지 않았군요')

st.subheader('Select box',divider=True)
fruit=st.selectbox('과일을 선택하세요',
             [':banana:바나나',':strawberry:딸기',':apple:사과',':melon:메론'],
                   index=None,
                   placeholder='과일을 선택해요!',
                   label_visibility='collapsed'
             )
st.write(f'당신이 선택한 과일은 {fruit}')

st.divider()
st.subheader('select box 예시코드')
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.divider()

st.subheader('Multiselect')
colors=st.multiselect('당신이 좋아하는 색상은?',
['red','green','blue','yellow','pink'])

st.write('선택한 색상은 ',colors)

st.subheader('Selectslider')
color=st.select_slider('당신이 좋아하는 색상은?',
                 options=['red','green','blue','yellow','brown','violet','indigo','orange']
                       )
color

color_st,color_end=st.select_slider('당신이 좋아하는 색상은?',
                 options=['red','green','blue','yellow','pink','violet','indigo','orange'],
                        value=('blue','pink')
                       )
st.write(f'당신이 좋아하는 색상은; {color_st},{color_end}')

satisfaction=st.select_slider('당신의 만족도는?',
                 options=range(10),value=5
                              )
satisfaction

st.subheader('Color picker')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.header('3. Numeric Input elements')
st.subheader('Numeric input')
# num=st.number_input('숫자 입력', min_value=0, max_value=100, step=2,
#                     format='%d')
# st.write(f'현재숫자: {num}')

num=st.number_input('숫자 입력', min_value=-10.0, max_value=10.0, step=2.0,
                    format='%f')
st.write(f'현재숫자: {num}')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)



# numf=st.number_input('숫자 입력',
#                      min_value=0.0,
#                      max_value=100.0,
#                      step=0.5,
#                      value=10.0,20.0,
#                      format='%f')

st.divider()

st.header('4. Text input elements')
st.subheader('Text input')
id=st.text_input('아이디:')
pw=st.text_input('비밀번호:',type='password')
st.write(f'아이디: {id}, 비밀번호: {pw}')

st.divider()

st.subheader('Text Area')
text=st.text_area('질문을 입력하세요')
st.write(text)
st.write(f'총 문자 길이는 {len(text)}')

st.header('5. Date&Time input elements')
st.subheader('Date input')
from datetime import datetime, date, time, timedelta

date=st.date_input('일자 선택',value=date(2024,3,1),
                   min_value=date(2023,1,1),
                   max_value=date(2024,12,31),
                   format='YYYY.MM.DD')
st.write(date)

st.subheader('Time input')
time=st.time_input('시간 입력',
              value=time(8,00),
              # step=timedelta(minutes=10)
              step=900
              )

import time
with st.spinner('wait for it'):
     time.sleep(5)
     st.balloons()
     st.success('Done!')
#
# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)
#
# for percent_complete in range(100):
#     time.sleep(0.01)
#     my_bar.progress(percent_complete + 1, text=progress_text)
# time.sleep(1)
# my_bar.empty()
#
# st.button("Rerun")

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')