import requests

OLLAMA_URL = "https://dominoes-perish-plant.ngrok-free.dev"

def get_hint(problem, code):

    prompt = f"""
あなたはプログラミング学習支援AIです。
答えは出さずヒントのみ出してください。

問題:
{problem}

コード:
{code}
"""

    res = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return res.json()["response"]