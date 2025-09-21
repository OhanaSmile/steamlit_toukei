## ここで各分布を組み立てる

import streamlit as st
from functions import function as fn

def cal_binom():
    st.markdown('### 1×2 母比率検定 早見アプリ') 
    # 対象データの入力
    n, k, p, arternative = fn.input_data()
    conf_level, ci_method, method_label = fn.setting_conf()

    # 計算ボタン
    if st.button('p値を計算'):
        fn.create_binom(k, n, p, arternative, conf_level, ci_method, method_label)



def pop_prop_diff():
    st.write('準備中')