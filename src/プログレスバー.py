import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image as image
import time


#
st.title("Streamlit 入門")
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!!'
#エクスパンダー FAQで使用するもの
expdander = st.beta_expander('問い合わせ1')
expdander.write('回答1')
expdander2 = st.beta_expander('問い合わせ2')
expdander2.write('回答2')
expdander3 = st.beta_expander('問い合わせ3')
expdander3.write('回答3')
