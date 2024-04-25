# 뉴스 데이터 kor_news_20240326.xlsx를 이용하여 스트림릿으로 구현하기

import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
import json

# 1.뉴스데이터를 dataframe으로 표시하기

st.subheader('1. 뉴스데이터를 dataframe으로 표시하기')

st.markdown('2024년 3월 26일 뉴스 데이터프레임')


def preprocess(df):
    df['분류리스트']=df.분류.str.split('>')


@st.cache_data
def load_data(file_path,index_col,header):
    df=pd.read_excel(file_path,index_col=index_col,header=header)
    return df

df_news=load_data('data/kor_news_240326.xlsx', index_col='식별자',header=0)
# df_news=pd.read_excel('data/kor_news_240326.xlsx', index_col='식별자',header=0)
# st.dataframe(df_news)

# 2.뉴스데이터의 url 컬럼을 실제 뉴스기사 페이지로 이동하도록 적절한  column configuration 사용

st.subheader('2.뉴스데이터의 url 컬럼을 실제 뉴스기사 페이지로 이동하도록 적절한  column configuration 사용')

st.dataframe(df_news,
             column_config={
                 'URL':st.column_config.LinkColumn(
                     help='News Links',
                     max_chars=100,
                     validate = '^https://www\.[a-z]+\.[a-z]+',
                     display_text='News 바로가기'
                 )})


# 3.분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기

st.subheader('3.분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기')

df_news['대분류']=['']*len(df_news)
for i, cat in enumerate(df_news['분류']):
    cat_split=cat.split('>')
    df_news.at[i,'대분류']=cat_split[0]
# df_news[:10]

from konlpy.tag import Okt
from collections import Counter
def word_count(dframe,column_name):
    cont = list(dframe[column_name])
    content = ', '.join(cont)
    okt = Okt()
    token_tag = okt.pos(content)
    token_list = [token for token, tag in token_tag
                  if (len(token) > 1) and (tag == 'Noun')]
    count = Counter(token_list)
    df = pd.DataFrame(pd.Series(count), columns=['Freq'])
    df = df.sort_values(by='Freq', ascending=False)
    return df

df_news_cat1 = word_count(df_news,'대분류')

df_news_cat1[:10]
# df_news_cat1.columns=['cat_word','Freq']

st.bar_chart(df_news_cat1,y='Freq')

# 4.제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기

import matplotlib.pyplot as plt

st.subheader('4.제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기')

df_news_ecosoc=df_news[(df_news['대분류']=='경제')|(df_news['대분류']=='사회')]
df_news_ecosoc['제목'] = df_news_ecosoc['제목'].astype(str)
df_news_title=word_count(df_news_ecosoc,'제목')
df_news_title=df_news_title[:20].sort_values('Freq',ascending=False)
st.bar_chart(df_news_title,y='Freq')
# df_news_title