# 🧠 Python学習支援AI（Ollama版）

Streamlit を使用して作成した、
初心者向けPython学習支援アプリです。

コード入力と問題文をもとに、ローカルLLM（Ollama）を使用して
「答えを直接出さずにヒントだけを提示するAI学習支援」を行います。

一定時間操作がない場合や、ヒントボタンを押した際にAIが動作し、
学習者の思考を妨げずに段階的なヒントを提供します。
---
## 🌐 URL

以下のURLからアプリにアクセスできます
(https://blank-app-60hp1dls0a6.streamlit.app/)

---

## 🌟 主な機能

### 💡 AIヒント機能（Ollama連携）
- 問題文とコードを入力するとAIがヒントを生成
- 正解コードは出さず、考え方のみ提示
- ローカルLLM（Ollama）を使用した安全な学習支援
- llama3などのモデルに対応

### ⌨️ コード入力型学習
- 問題文とコードを同時に入力可能
- 学習者の現在の思考状態をもとにヒント生成
- デバッグ・アルゴリズム理解の補助

### 🧠 思考支援型ヒント設計
- 「どこが間違っているか」
- 「次に考えるべきポイント」
- 「改善の方向性」
のみを提示し、答えは出さない設計

### 🌐 ローカルLLM対応（Ollama）
- OpenAI APIを使用せず完全ローカルで動作可能
- インターネット不要のAI環境
- プライバシーを考慮した学習支援

### 🔗 ngrok連携
- ローカルで動くOllamaを外部公開
- Codespacesやクラウド環境からアクセス可能
- 開発・実験用の簡易API構成

---

## 🛠 セットアップ方法
### 1. 必要なライブラリのインストール
Python環境がインストールされていることを確認し、必要なライブラリをインストールして下さい
```bash
pip install streamlit requests streamlit-ace
```
#### 役割
| ライブラリ         | 用途              |
| ------------- | --------------- |
| streamlit     | UI（画面全体）        |
| requests      | OllamaへAPI通信    |
| streamlit-ace | コードエディタ（st_ace） |

### 2. Ollamaのインストール

以下からインストール：

(https://ollama.com/)

### 3. モデルの実行(ターミナルで実行)（1度だけでいい）

```bash
ollama run llama3
```

### 4. ngrokのインストール（外部アクセス用）
以下からインストール：

(https://ngrok.com/)
### 5. ngrokの実行（ターミナルで実行・アプリ使用の際実行必須）

```bash
ngrok http 11434 --host-header="localhost:11434"
```

### 6. Streamlitアプリの起動
```bash
streamlit run streamlit_app.py
```
---
## 🔌 システム構成
```text
Streamlit（UI）
   ↓
Pythonコード
   ↓
ngrok（トンネル）
   ↓
Ollama（ローカルLLM）
   ↓
ヒント生成
```
---
## 🧩 ファイル構成
| ファイル名        | 内容　　           |
| ------------- | --------------- |
|streamlit_app.py|	メインUI|
|ai_hint.py|	Ollamaとの通信処理|
|requirements.txt|	依存ライブラリ|
|ngrok	|外部公開用トンネル|

---

## 🧠 AIヒントの仕組み

AIには以下の制約を与えています：

- 正解コードを出さない
- 解説ではなく「気づき」を与える
- 次に考えるべき方向性を提示
---

## 💻 使用技術
* **Python**
* **Streamlit（UI）**(https://streamlit.io/)
* **Ollama（ローカルLLM）**(https://ollama.com/)
* **ngrok（外部公開）**(https://ngrok.com/)
* **requests（API通信）**

---

## 🚀 今後のロードマップ
- 手詰まり検知の自動化（無操作検出）
- ヒントレベル（Lv1〜Lv3）の導入
- コード実行結果との連動
- 学習履歴の保存機能
- 複数モデル比較（llama3 / mistral / phi3）

---
## 🧠 このプロジェクトの特徴

このアプリは単なるチャットAIではなく、

👉 「考えさせるAI学習支援システム」

として設計されています。
