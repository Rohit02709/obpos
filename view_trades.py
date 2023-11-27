import requests
import streamlit as st
import pandas as pd
from decimal import Decimal

URL=r'https://7z3vkun3jxdpyai7ludlptbzdq0ccori.lambda-url.ap-south-1.on.aws/'
resp=requests.get(URL,json={'operation':'scan_orders'})
df=pd.DataFrame(eval(resp.text))

df['pd_time']=pd.to_datetime(df['date'].astype(str)+df['time'],format='%Y%m%d%H:%M:%S')
df.sort_values('pd_time',inplace=True)
df.drop('tag',inplace=True,axis=1)
df.reset_index(inplace=True,drop=True)
st.dataframe(df)