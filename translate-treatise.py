import streamlit as st

st.title("トラトラトラ🐯🐯")
st.write("論文を翻訳します。時間はかかります。")    

uploaded_file = st.file_uploader("PDFをアップロードしてください。", type = ["pdf"])

engine = st.selectbox("翻訳として利用するサービスを選択してください。", ["Gemini", "ChatGPT-4o"])
