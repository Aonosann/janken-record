import streamlit as st
import csv
import os
import pandas as pd
from datetime import datetime

# ファイル名を決める
RECORD_FILE = "record.csv"

st.title("じゃんけん戦績記録アプリ")

# ファイルが存在するか確認して、なければ作る
if not os.path.exists(RECORD_FILE):
    with open(RECORD_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['勝敗', '日時'])
    st.write("新しく記録ファイルを作りました！")

# ファイルの中身を読み込む
df = pd.read_csv(RECORD_FILE)

# 統計を表示
st.subheader("通算成績")
win_count = len(df[df['勝敗'] == '勝ち'])
lose_count = len(df[df['勝敗'] == '負け'])
st.write(f"**{win_count}勝 {lose_count}敗**")

# 記録を表示
st.subheader("試合履歴")
st.dataframe(df)

# ボタンを横並びに
col1, col2 = st.columns(2)

with col1:
    if st.button("勝ち 🎉"):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(RECORD_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['勝ち', now])
        st.rerun()

with col2:
    if st.button("負け 😢"):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(RECORD_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['負け', now])
        st.rerun()
# リセットボタン
st.divider()  # 区切り線
if st.button("🗑️ 記録をリセット", type="secondary"):
    if os.path.exists(RECORD_FILE):
        os.remove(RECORD_FILE)  # ファイルを削除
        st.success("記録をリセットしました！")
        st.rerun()