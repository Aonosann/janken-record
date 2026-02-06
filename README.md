# じゃんけん戦績記録アプリ
Streamlitを使った3本先取じゃんけんゲームに戦績記録機能を追加したアプリです。

## 機能

- 3本先取のじゃんけんゲーム
- 勝敗を自動記録
- 通算成績と勝率の表示
- 過去の試合履歴の確認

## 使い方

### 環境構築
```bash
# リポジトリをクローン
git clone https://github.com/Aonosann/janken-record.git
cd janken-record

# 仮想環境を作成
python -m venv .venv

# 仮想環境を有効化
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

# 必要なライブラリをインストール
pip install -r requirements.txt
```

### 実行
```bash
streamlit run janken_game.py
```

## 学んだこと

- 仮想環境の使い方
- CSVファイルの読み書き
- pandasでのデータ処理
- Streamlitのsession_state管理
- Gitの基本的な使い方

## リポジトリ

https://github.com/Aonosann/janken-record