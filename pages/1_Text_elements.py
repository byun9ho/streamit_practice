import numpy as np
import pandas as pd

import streamlit as st

st.title('Streamlit 맛보기')
st.header('1. 텍스트 요소',divider='rainbow')
st.subheader('1.1 제목 요소를 작성하기 위한 API',divider=True)

st.write('Hello _Streamlit_ :cool: :sunglasses: :horse:')

st.write('''st.title()  
st.header()

st.subheader()
''')


st.subheader('1.2 테스트 _본문_ 을 구성하는 :red[API]')

st.write('''
st.caption()  
st.text()  
st.code()  
st.markdown()  
st.latex()

''')

st.text('This is some text')
st.caption('This is a caption')
st.write('st.markdown()')
st.markdown('''한 줄 끝에 입력한 두칸의 공백(space)은  
 다음 줄로 사용(soft return)
 
 한 행에 두 개 이상의 newline은 hard return이 됨
''')

sample_code='''
def fun():
    print('Hello!!!')
    
'''
st.write(':blue[st.code]')
st.code(sample_code,language='python')

st.write('---')
st.write('[st.latex]')
st.latex('b \over a')
st.latex('\sqrt{x^2+y^2}')
st.divider()
st.write('Emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ ')

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')
#
# with st.echo():
#     st.write('This code will be printed')

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')