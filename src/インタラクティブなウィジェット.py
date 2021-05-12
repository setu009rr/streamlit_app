import streamlit as st

from PIL import Image as image


#
st.title("Streamlit 入門")

# テキストボックス
text = st.text_input('あなたの趣味を入力してください')
'あなたの趣味は', text, 'です'

#スライダー
condition = st.slider('調子はいかが？',0, 100, 50)
'あんたのコンディションは', condition, 'ですね'

# セレクトボックスで値を入力する
# st.write('Interactive Widget')
# option = st.selectbox(
#     '好きな数字を入力してください',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です'

# チェックボックスで画像出力の有無を選択する
# if st.checkbox('Show image'):
#     img = image.open("C:\\Users\\mglns\\PycharmProjects\\stremlit_test\\picture\\goro_1.jpg")
#     st.image(img, caption='gorochan', use_column_width=True)
