import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_hint(problem, code):

    prompt = f"""
あなたはPython講師です。

問題:
{problem}

コード:
{code}

絶対に答えを書かない。

以下のみ答える。

・今何をしようとしているか
・不足している考え方
・次に確認すべきこと
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content