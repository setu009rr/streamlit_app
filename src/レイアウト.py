import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image as image


#
st.title("Streamlit 入門")
st.write('Interactive Widgets')

#エクスパンダー FAQで使用するもの
expdander = st.beta_expander('問い合わせ1')
expdander.write('回答1')
expdander2 = st.beta_expander('問い合わせ2')
expdander2.write('回答2')
expdander3 = st.beta_expander('問い合わせ3')
expdander3.write('回答3')


#カラム利用レイアウト
# left_column, right_column = st.beta_columns(2)
# buttun = left_column.button('右カラムに文字を表示')
# if buttun:
#     right_column.write('ここは右のカラム')

# サイドバーの例
# text = st.text_input('あなたの趣味を入力してください')
# 'あなたの趣味は', text, 'です'

# condition = st.slider('調子はいかが？',0, 100, 50)
# 'あんたのコンディションは', condition, 'ですね'

# セレクトボックスで値を入力する
# option = st.selectbox(
#     '好きな数字を入力してください',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です'

# チェックボックスで画像出力の有無を選択する
# if st.checkbox('Show image'):
#     img = image.open("C:\\Users\\mglns\\PycharmProjects\\stremlit_test\\picture\\goro_1.jpg")
#     st.image(img, caption='gorochan', use_column_width=True)
