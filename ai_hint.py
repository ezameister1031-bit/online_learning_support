import requests

OLLAMA_URL = "https://dominoes-perish-plant.ngrok-free.dev"

def get_hint(problem, code):

    prompt = f"""
あなたはプログラミング講師です。
答えは出さずヒントのみ出してください。

問題:
{problem}

コード:
{code}
"""

    try:
        res = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        },
        timeout=30
    )

    st = res.status_code
    print("status =", st)
    print("response text =", res.text)

    data = res.json()
    return str(data)

    return data.get("response", "AIからの応答がありません")

    except Exception as e:
        return f"エラー: {str(e)}"
