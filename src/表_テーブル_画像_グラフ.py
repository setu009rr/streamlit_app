import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image as image


# 表・画像出力などのまとめ
st.title("Streamlit 入門")
# st.write("Data frame")

# 表の作成例。dataframeを使うと動的な表が作成できる。静的な表の場合はtableを使用する
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 300, 40]})

st.dataframe(df, width=1500, height=1500)
# st.table(df.style.highlight_max(axis=0))

#マークダウン記法例
# """
# # 章
# ## 説
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
#
# ```
# """

# グラフの作成例。line_chart→折れ線グラフ。area_chart→折れ線グラフのエリアに色塗りされたグラフ
# bar_chart→棒フラグ
# df = pd.DataFrame(
#     np.random.rand(20, 3)
# ,columns=['a', 'b', 'c'])
#
# df
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# 0を中心に正規分布した値に新宿の緯度と経度を足して、その結果をマップ上に反映する
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon'])
# st.map(df)

#画像出力
# st.write('Display Image')
# img = image.open("C:\\Users\\mglns\\PycharmProjects\\stremlit_test\\picture\\goro_1.jpg")
# st.image(img, caption='gorochan', use_column_width=True)