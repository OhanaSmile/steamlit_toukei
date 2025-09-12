##---------------------------------
# アプリ仕様（シンプル版）
## 入力
### サンプルサイズ N（試行回数）
### 成功数（度数）

## 処理
### 帰無仮説 p=0.5 として 二項検定 (binom test) を実施
### 片側 p値を計算

## 出力
### 計算した p値を表示
##---------------------------------

import streamlit as st
from scipy.stats import binomtest
import numpy as np

st.title('1×2 母比率検定 早見アプリ')

sep_001, sep_002 = st.columns(2)
# 入力
with sep_001:
    N = st.number_input('試行回数 N', min_value=1, step=1, value=10)
with sep_002:
    k = st.number_input('成功数 （度数）', min_value=0, step=1, value=5, max_value=N)

# 計算ボタン
if st.button('p値を計算'):
    # 二項検定
    result = binomtest(k, n=N, p=0.5, alternative='greater')
    p_value = result.pvalue

    # 出力
    st.subheader('計算結果')
    st.write(f'**N={N}, 成功数={k}の場合の片側p値：**')
    st.metric(label='p値', value=f'{np.round(p_value, 3)}')


