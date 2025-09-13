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

font_path = "font/NotoSansJP-Regular.ttf"
fm.fontManager.addfont(font_path)
mpl.rcParams["font.family"] = fm.FontProperties(fname=font_path).get_name()

 
# --メイン関数--
def main():
    st.markdown('### 1×2 母比率検定 早見アプリ') 
    # 対象データの入力
    n, k, p = fn.input_data()

    conf_level, ci_method, method_label = fn.setting_conf()

    # 計算ボタン
    if st.button('p値を計算'):
        fn.create_binom(k, n, p, conf_level, ci_method, method_label)



#  --- スクリプトとして実行されたときだけ main() を呼ぶ ---
if __name__ == '__main__':
    main()


