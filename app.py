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
import numpy as np
import matplotlib.font_manager as fm
import matplotlib as mpl
from functions import function as fn
from functions import category as cat

font_path = "font/NotoSansJP-Regular.ttf"
fm.fontManager.addfont(font_path)
mpl.rcParams["font.family"] = fm.FontProperties(fname=font_path).get_name()

 
# --メイン関数--
def main():
    stats_kind = st.radio('メニュー', options=['1×2 母比率検定', '母比率不等'], index=0)
    st.markdown('---')
     # メニューに応じて関数を呼び出す
    if stats_kind == '1×2 母比率検定':
        cat.cal_binom()
    elif stats_kind == '母比率不等':
        cat.pop_prop_diff()



#  --- スクリプトとして実行されたときだけ main() を呼ぶ ---
if __name__ == '__main__':
    main()
