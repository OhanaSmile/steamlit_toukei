import streamlit as st
from scipy.stats import binomtest, binom
import numpy as np
import matplotlib.pyplot as plt



def input_data():
    sep_001, sep_002, sep_003 = st.columns(3)
    # 入力
    with sep_001:
        N = st.number_input('試行回数 N', min_value=1, step=1, value=10)
    with sep_002:
        p = st.number_input('成功確率', min_value=0.00, step=0.01, value=.50, max_value=1.00)
    
    sep_0011, sep_0021, sep_0031 = st.columns(3)
    with sep_0011:
        k = st.number_input('成功数 （度数）', min_value=0, step=1, value=5, max_value=N)
        z = k / N
        st.write(f'成功率: {z:.3f}')

    st.markdown('---')
    
    sep_0012, sep_0022 = st.columns(2)
    with sep_0012:
        arternative = st.radio('片側？両側？', options=['greater', 'less', 'two-sided'], index=0, horizontal=True)  # 'two-sided', 'less', 'greater'

    return N, k, p, arternative

def setting_conf():
    # 追加: 信頼水準と手法をUIで指定（任意）
    sep_101, sep_102, sep_103 = st.columns(3)
    with sep_101:
        conf_level = st.slider('信頼水準', min_value=0.80, max_value=0.99, value=0.95, step=0.01)
    with sep_102:
        method_label = st.selectbox('信頼区間の方法', ['Wilson']) # , 'Wilson (CC: 連続性補正)', 'Clopper-Pearson (Exact)'
        method_map = {
            'Wilson': 'wilson',
            'Wilson (CC: 連続性補正)': 'wilsoncc',
            'Clopper-Pearson (Exact)': 'exact',
        }
        ci_method = method_map[method_label]
    return conf_level, ci_method , method_label



def create_binom(k, N, p, arternative, conf_level, ci_method, method_label):
    result = binomtest(k, n=N, p= p, alternative= arternative)  # 'two-sided' 'less' 'greater'
    p_value = result.pvalue

    # 出力
    st.subheader('計算結果')
    st.write(f'**N={N}, 成功数={k}の場合の片側p値：**')
    st.metric(label='p値', value=f'{np.round(p_value, 3)}')


    ## ここに信頼区間を計算するコードを書く。
    ci = result.proportion_ci(confidence_level= conf_level, method=ci_method)
    ci_low, ci_high = float(ci.low), float(ci.high)
    st.metric(label=f'{int(conf_level*100)}% 信頼区間 (p)', value=f'[{ci_low:.3f}, {ci_high:.3f}]')
    st.caption(f'方法: {method_label}')


    # グラフ表示------------------------------
    x = np.arange(0, N + 1)
    pmf = binom.pmf(x, N, p)

    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(x, pmf, color='lightblue' ,align='center') 

    for i, b in enumerate(bars):
        if i >= k:
            b.set_color('orange')

    ax.axvline(k, color='red', linestyle='--', label='成功数の位置')
    ax.text(k, max(pmf)*0.9, f'成功数={k}', color='red', fontsize=10, ha='center', va='top')
    # 軸・タイトル
    ax.set_xlabel('成功数 x')
    ax.set_ylabel(f'P(X = x | N, p={p})')
    ax.set_title(f'二項分布 PMF（H0: p={p}）と片側領域（x ≥ k）')

        # p値を図中に表示
    ax.text(
        0.98, 0.95,
        f'p値（x ≥ {k}）= {p_value:.3f}',
        transform=ax.transAxes, ha='right', va='top',
        bbox=dict(boxstyle='round', alpha=0.2)
    )
    st.pyplot(fig)


