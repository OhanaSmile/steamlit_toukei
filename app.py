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

st.title('1×2 母比率検定 早見アプリ')

sep_001, sep_002 = st.columns(2)
# 入力
with sep_001:
    N = st.number_input('試行回数 N', min_value=1, step=1, value=10)
with sep_002:
    k = st.number_input('成功数 （度数）', min_value=0, step=1, value=5, max_value=N)

# 計算ボタン



