#연습문제2

import streamlit as st
import seaborn as sns
import pandas as pd

# 1. iris 데이터셋을 이용하여
# 1) iris 데이터셋을 데이터프레임으로 표시

df_iris=sns.load_dataset('iris')
st.dataframe(df_iris.head())
st.write(df_iris.species.unique())

# 2) multiselect를 사용하여 품종(species)을 선택하면 해당 품종의 데이터에 대한 데이터프레임으로 표시

st.subheader('품종선택', divider=True)

selected_species=st.multiselect('좋아하는 품종은?',
                 ['setosa','versicolor','virginica'],
                       )

if selected_species:
    df_selected = df_iris[df_iris['species'].isin(selected_species)]
    st.write('선택하신 품종에 대한 통계치:')
    st.dataframe(df_selected.groupby('species').mean())
else:
    st.write('품종을 선택하세요.')

# 3) 품종을 제외한 4가지 컬럼을 radio 요소를 사용하여 선택하면 선택한 컬럼에 대한 히스토그램을 그리기(matplotlib)

import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

st.subheader('히스토그램을 보여줄 컬럼 선택',divider=True)

column_list=df_iris.columns[:-1].tolist()
col=st.radio(
    '히스토그램을 보고 싶은 컬럼은?', column_list)

fig=plt.figure()
plt.hist(df_iris[col])
plt.title(f'선택한 {col}컬럼의 히스토그램')
st.pyplot(fig)

# 2. kor_news 데이터셋을 이용 분류의 대분류 기준을 선택하면 해당 분야의 주요 키워드 20위에 대한 barchart표시

# st.subheader('1. 뉴스데이터를 dataframe으로 표시하기')
#
# st.markdown('2024년 3월 26일 뉴스 데이터프레임')
#
# df_news=pd.read_excel('data/kor_news_240326.xlsx', index_col='식별자',header=0)
#
# df_news['대분류']=['']*len(df_news)
# for i, cat in enumerate(df_news['분류']):
#     cat_split=cat.split('>')
#     df_news.at[i,'대분류']=cat_split[0]
#
# cat1=df_news[:-2].대분류.unique().tolist()
# sel=st.radio('키워드를 확인하고 싶은 대분류를 선택하시오(1개)',cat1)
# selected=df_news[df_news[대분류]==sel].본문
#
# selected=selected['본문'].astype(str)
#
# from konlpy.tag import Okt
# from collections import Counter
# def word_count(dframe,column_name):
#     cont = list(dframe[column_name])
#     content = ', '.join(cont)
#     okt = Okt()
#     token_tag = okt.pos(content)
#     token_list = [token for token, tag in token_tag
#                   if (len(token) > 1) and (tag == 'Noun')]
#     count = Counter(token_list)
#     df = pd.DataFrame(pd.Series(count), columns=['Freq'])
#     df = df.sort_values(by='Freq', ascending=False)
#     return df
#
# df_news_article=word_count(selected,'본문')
# df_news_chart=df_news_article.sort_values('Freq',ascending=False)
# df_news_chart=df_news_chart[:20]
# st.bar_chart(df_news_chart,y='Freq')

from konlpy.tag import Okt
from collections import Counter

st.subheader('1. 뉴스데이터를 dataframe으로 표시하기')
st.markdown('2024년 3월 26일 뉴스 데이터프레임')

# 뉴스 데이터프레임 로드
df_news = pd.read_excel('data/kor_news_240326.xlsx', index_col='식별자', header=0)

# 대분류 추가
df_news['대분류'] = [''] * len(df_news)
for i, cat in enumerate(df_news['분류']):
    cat_split = cat.split('>')
    df_news.at[i, '대분류'] = cat_split[0]

cat1 = df_news[:-2].대분류.unique().tolist()

# 대분류 선택
sel = st.radio('키워드를 확인하고 싶은 대분류를 선택하시오(1개)', cat1)

# 선택된 대분류에 해당하는 본문 가져오기
selected = df_news[df_news['대분류'] == sel]['본문'].astype(str)

# 단어 빈도수 계산 함수 정의(어제 숙제 재활용)
def word_count(dframe, column_name):
    cont = list(dframe)
    content = ', '.join(cont)
    okt = Okt()
    token_tag = okt.pos(content)
    token_list = [token for token, tag in token_tag
                  if (len(token) > 1) and (tag == 'Noun')]
    count = Counter(token_list)
    df = pd.DataFrame(pd.Series(count), columns=['Freq'])
    df = df.sort_values(by='Freq', ascending=False)
    return df

# 선택된 대분류에 대한 단어 빈도수 계산
df_news_article = word_count(selected, '본문')
df_news_chart = df_news_article.sort_values('Freq', ascending=False)[:20]

# 결과 표시(정렬은 단어 가나다순)
st.bar_chart(df_news_chart, y='Freq')

# 3. 경기도인구데이터에 대하여

# 1) 연도별 인구수에 대한 지도시각화
# 2007년, 2015년, 2017년 연도를 탭으로 제시

st.header('3. 경기도인구데이터 연도별 탭사용 지도시각화')

import json
import folium
from streamlit_folium import st_folium

@st.cache_data
def load_geo_json(file_path):
    with open(file_path, encoding='utf-8') as f:
        geo_gg=json.loads(f.read())
    return geo_gg

@st.cache_data
def load_excel(file_path):
    df_gg=pd.read_excel(file_path, index_col='구분')
    return df_gg

json_file='c://workspace_Multi07/09_streamlit/webDash/data/경기도행정구역경계.json'
excel_file='c://workspace_Multi07/09_streamlit/webDash/data/경기도인구데이터.xlsx'

geo_gg=load_geo_json(json_file)
df_gg=load_excel(excel_file)
st.dataframe(df_gg)

def map_draw(yr):
    map = folium.Map(location=[37.574, 126.973], zoom_start=8)
    folium.GeoJson(geo_gg).add_to(map)
    folium.Choropleth(geo_data=geo_gg,
                      data=df_gg[yr],
                      columns = [df_gg.index, df_gg[yr]],
                      key_on = 'feature.properties.name').add_to(map)
    st_folium(map, width=600, height=400)

tab1, tab2, tab3 = st.tabs(['2007', '2015', '2017'])
with tab1:
    st.subheader('2007')
    yr=2007
    map_draw(yr)

with tab2:
    st.subheader('2015')
    yr=2015
    map_draw(yr)

with tab3:
    st.subheader('2017')
    yr=2017
    map_draw(yr)

# END #