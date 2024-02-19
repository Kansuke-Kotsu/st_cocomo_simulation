import streamlit as st
import pandas as pd
import numpy as np

def caliculation(initial_bed):
        # 1列目
        num = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        # 2列目
        bed = np.array([1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4081])
        # 3列目
        total = np.array([1,2,4,7,12,20,33,54,88,143,232,376,609,986,1596,2582, 4178,6760,10938])
        # 4列目
        benefit = initial_bed * (bed * 3 - total)
        # 5列目
        rate = []
        for i in range (len(num)):
                rate.append((2/3)**num[i])
        # 表を描画
        data = {
                '回数': num,
                '掛け金': bed * initial_bed,
                'トータル': total * initial_bed,
                '利益': benefit,
                '負け確率': rate
                }
        df = pd.DataFrame(data)
        return df


def main():
        # Streamlitアプリケーションの作成
        st.title('ココモ法 シミュレーション')
        initial_bed = st.number_input("input initial bet", step=500, value=0)
        if  initial_bed:
                df = caliculation(initial_bed=initial_bed)
                st.table(df)

if __name__ == '__main__':
        main()
