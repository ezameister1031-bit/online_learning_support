import google.generativeai as genai
import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def get_hint(problem, code):

    prompt = f"""
あなたは優秀なPython講師です。

以下のルールを必ず守ってください。

【ルール】
・答えを書かない
・完成コードを書かない
・考えるヒントだけ出す
・初心者向けに説明する
・次に確認すべきポイントを教える

問題:
{problem}

学習者のコード:
{code}
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:
        return f"エラー: {e}"
