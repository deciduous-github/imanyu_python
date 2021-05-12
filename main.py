import streamlit as st

st.title('Streamlit 超入門')

user_name = st.text_input("ユーザーネーム")
'あなたのユーザーネームは:', user_name

user_pass = st.text_input('パスワード')
'あなたのパスワードは：', user_pass

print(user_name)
print(user_pass)
