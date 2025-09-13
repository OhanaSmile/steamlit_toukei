import streamlit as st
from scipy.stats import binomtest, binom
import numpy as np
import matplotlib.pyplot as plt



def input_data():
    sep_001, sep_002 = st.columns(2)
    # 入力
    with sep_001:
        N = st.number_input('試行回数 N', min_value=1, step=1, value=10)
    with sep_002:
        k = st.number_input('成功数 （度数）', min_value=0, step=1, value=5, max_value=N)

    return N, k


def create_binom(k, N):
    result = binomtest(k, n=N, p=0.5, alternative='greater')
    p_value = result.pvalue

    # 出力
    st.subheader('計算結果')
    st.write(f'**N={N}, 成功数={k}の場合の片側p値：**')
    st.metric(label='p値', value=f'{np.round(p_value, 3)}')

    # グラフ表示
    x = np.arange(0, N + 1)
    pmf = binom.pmf(x, N, 0.5)

    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(x, pmf, color='lightblue' ,align='center') 

    for i, b in enumerate(bars):
        if i >= k:
            b.set_color('orange')

    ax.axvline(k, color='red', linestyle='--', label='成功数の位置')
    ax.text(k, max(pmf)*0.9, f'成功数={k}', color='red', fontsize=10, ha='center', va='top')
    # 軸・タイトル
    ax.set_xlabel('成功数 x')
    ax.set_ylabel('P(X = x | N, p=0.5)')
    ax.set_title('二項分布 PMF（H0: p=0.5）と片側領域（x ≥ k）')

        # p値を図中に表示
    ax.text(
        0.98, 0.95,
        f'p値（x ≥ {k}）= {p_value:.3f}',
        transform=ax.transAxes, ha='right', va='top',
        bbox=dict(boxstyle='round', alpha=0.2)
    )
    st.pyplot(fig)


