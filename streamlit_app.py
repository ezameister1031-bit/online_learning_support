import streamlit as st
import time
from streamlit_ace import st_ace
from ai_hint import get_hint

import io
import contextlib

def run_code(code):
    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code)

        return output.getvalue()

    except Exception as e:
        return f"エラー:\n{e}"
st.title("Python学習支援システム")

# 問題入力
problem = st.text_area(
    "問題文",
    height=200
)

st.write("コード")

# コード入力
code = st_ace(
    language="python",
    theme="github",
    height=400,
    key="code_editor"
)
if st.button("コードを実行"):
    result = run_code(code)

    st.subheader("実行結果")
    st.code(result)
# ヒントボタン
with st.form("hint_form"):
    submitted = st.form_submit_button("ヒントをもらう")
    if submitted:
        st.write(get_hint(problem, code))

# =========================
# 停止時間の計測
# =========================

if "last_code" not in st.session_state:
    st.session_state.last_code = ""
    st.session_state.last_time = time.time()

# コードが変わったら時間リセット
if code != st.session_state.last_code:
    st.session_state.last_code = code
    st.session_state.last_time = time.time()

# 停止時間計算
idle_time = time.time() - st.session_state.last_time

st.write(f"停止時間: {int(idle_time)}秒")

# =========================
# 自動ヒント
# =========================

IDLE_LIMIT = 30

if idle_time > IDLE_LIMIT:
    st.warning("悩んでいる？ヒントをあげるよ")

    hint = get_hint(problem, code)
    st.info(hint)
