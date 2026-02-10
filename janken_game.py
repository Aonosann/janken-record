import streamlit as st
import random
import csv
import os
import pandas as pd
from datetime import datetime

# ファイル名を決める
RECORD_FILE = "record.csv"

# 戦績を記録する関数
def save_record(result):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(RECORD_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([result, now])

# ファイルが存在するか確認して、なければ作る
if not os.path.exists(RECORD_FILE):
    with open(RECORD_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['勝敗', '日時'])

# プレイヤーとCPUのスコアをセッションで管理
player = None
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.cpu_score = 0
    st.session_state.game_recorded = False  # 記録済みフラグを追加

# inputされた数字に対応する手を辞書で定義
hands = {
    "0": "グー ✊",
    "1": "チョキ ✌️",
    "2": "パー 🖐️"
}

# ゲームタイトル表示
st.title("3本先取じゃんけん！")

# 通算成績を表示（ゲーム開始前に表示）
df = pd.read_csv(RECORD_FILE)
win_count = len(df[df['勝敗'] == '勝ち'])
lose_count = len(df[df['勝敗'] == '負け'])
total_games = win_count + lose_count

# 勝率を計算（試合数が0の場合は0%）
if total_games > 0:
    win_rate = (win_count / total_games) * 100
    st.write(f"**通算成績: {win_count}勝 {lose_count}敗（勝率 {win_rate:.1f}%）**")
else:
    st.write("**通算成績: まだ記録がありません**")
    
# 戦績表を表示
with st.expander("戦績を見る"):
    st.dataframe(df)

st.divider()

# ゲームループSTART
if st.session_state.player_score < 3 and st.session_state.cpu_score < 3:
    st.write("ボタンを押して手を選んでね。")
    # ボタンで手を選択(カラムを使って横並びに配置)
    col1, col2, col3 = st.columns(3)
    if col1.button("グー ✊"):
        player = "0"
    if col2.button("チョキ ✌️"):
        player = "1"
    if col3.button("パー 🖐️"):
        player = "2"
    
    # 勝敗判定
    if player is not None:
        cpu = str(random.randint(0, 2))
        st.write(hands[player] + "を選んだ！")
        st.write("CPUの手は: " + hands[cpu])
        result = (int(player) - int(cpu) + 3) % 3
        
        # 結果表示とスコア更新
        if result == 0:
            st.write("引き分け！")
        elif result == 2:
            st.write("君の勝ち！🎉")
            st.session_state.player_score += 1
        else:
            st.write("君の負け...😢")
            st.session_state.cpu_score += 1
        
        # スコア表示
        st.write(f"スコア - 君: {st.session_state.player_score} | CPU: {st.session_state.cpu_score}")
        st.write("-------------------------")
        
        # ゲーム終了判定
        if st.session_state.player_score == 3 or st.session_state.cpu_score == 3:
            st.rerun()

# 最終結果表示
else:
    st.write("ゲーム終了！")
    st.write(f"最終スコア - 君: {st.session_state.player_score} | CPU: {st.session_state.cpu_score}")
    
    # 勝敗表示
    if st.session_state.player_score == 3:
        st.write("おめでとう！君の勝ち！🏆")
    else:
        st.write("残念！負けちゃった！💻")

    # 記録（まだ記録していない場合のみ）
    if not st.session_state.game_recorded:
        if st.session_state.player_score == 3:
            save_record('勝ち')
        else:
            save_record('負け')
        st.session_state.game_recorded = True

    # リセットボタン
    if st.button("もう一回！🔄"):
        st.session_state.player_score = 0
        st.session_state.cpu_score = 0
        st.session_state.game_recorded = False
        st.rerun()