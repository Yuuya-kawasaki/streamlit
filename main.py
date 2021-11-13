import streamlit as st
import time
st.title('streamlit 超入門')

st.write('プログレスバーの表示')

'stert!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text( f'Iteration {1+i}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ１回答')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ２回答')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ３回答')


text = st.text_input('あなたの趣味を教えてください')

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:',text
'コンディション:',condition

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です'

