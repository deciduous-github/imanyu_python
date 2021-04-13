import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
st.write('DateFlame')

df = pd.DataFrame({
    '一列目': [1, 2, 3, 4],
    '二列目': [10, 20, 30, 40],
})

# st.write(df)
# テキスト同様にデータフレームを表示させる場合はwrite

st.dataframe(df, width=500, height=100)
# DataFrameでも同じ表示ができるが、縦と横の長さが指定できる