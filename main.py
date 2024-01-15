import streamlit as st
import pandas as pd

# 3x10のデータを作成
data = {'Column 1': [1, 2, 3],
        'Column 2': [4, 5, 6],
        'Column 3': [7, 8, 9],
        'Column 4': [10, 11, 12],
        'Column 5': [13, 14, 15],
        'Column 6': [16, 17, 18],
        'Column 7': [19, 20, 21],
        'Column 8': [22, 23, 24],
        'Column 9': [25, 26, 27],
        'Column 10': [28, 29, 30]}

df = pd.DataFrame(data)

# Streamlitアプリケーションの作成
st.title('3x10の表を描画する')

# 表の描画
st.table(df)
