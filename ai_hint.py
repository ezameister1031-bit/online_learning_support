import requests

def get_hint_ollama(problem, code):

    prompt = f"""
あなたはプログラミング講師です。
絶対に答えを出さずヒントだけ出してください。

問題:
{problem}

コード:
{code}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
