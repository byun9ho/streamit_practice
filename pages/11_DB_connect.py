import streamlit as st

# mysql 연결(접속)

conn=st.connection('shopDB',
                   type='sql',
                   url='mysql://streamlit:1234@localhost:3306/shopDB')

# 질의 수행
df=conn.query('SELECT * FROM customer;',ttl=600)

st.write(df)
# list(df.itertuples())
for row in df.itertuples():
    st.write(f'{row.customer_name}이 {row.phone}을 가짐')

# query문을 text로 선언
from sqlalchemy import text
sql = text('INSERT INTO customer (customer_id, customer_name, phone, birthday) VALUES (:customer_id, :customer_name, :phone, :birthday)')

with conn.session as s:
    s.execute(sql, {'customer_id': 6, 'customer_name': "홍길동", 'phone': "010-111-1111", 'birthday': "2000-01-31"})
    # s.execute(sql)
    s.commit()
