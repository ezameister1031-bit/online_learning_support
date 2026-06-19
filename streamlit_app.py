import streamlit as st
from streamlit_autorefresh import st_autorefresh
import io
import contextlib



st_autorefresh(interval=1000, key="idle_check")
st.title("Python学習支援システム")

problem = st.text_area(
    "問題文",
    height=200
)

st.write("コード")

from streamlit_ace import st_ace

code = st_ace(
    language="python",
    theme="github",
    height=400,
    auto_update=True
)

st.subheader("実行結果")
if "run_output" not in st.session_state:
    st.session_state.run_output = ""
if "hint" not in st.session_state:
    st.session_state.hint = ""
if st.button("コード実行"):

    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code)

        st.session_state.run_output = output.getvalue()

    except Exception as e:
        st.session_state.run_output = f"エラー: {e}"
st.subheader("実行結果")

if st.session_state.run_output:
    st.code(st.session_state.run_output)
    
from ai_hint import get_hint

if st.button("ヒントをもらう"):
    st.session_state.hint = get_hint(problem, code)

st.write("DEBUG:", repr(st.session_state.hint))

if st.session_state.hint:
    st.info(st.session_state.hint)
import time
if "last_code" not in st.session_state:
    st.session_state.last_code = ""
    st.session_state.last_time = time.time()

if code != st.session_state.last_code:

    st.session_state.last_code = code
    st.session_state.last_time = time.time()

idle_time = (
    time.time()
    - st.session_state.last_time
)

st.write(
    f"停止時間: {int(idle_time)}秒"
)

IDLE_LIMIT = 30
if "auto_hint_given" not in st.session_state:
    st.session_state.auto_hint_given = False
if code != st.session_state.last_code:
    st.session_state.last_code = code
    st.session_state.last_time = time.time()
    st.session_state.auto_hint_given = False
if idle_time > IDLE_LIMIT:

    st.warning(
        "悩んでいる？ヒントをあげるよ"
    )

    if not st.session_state.auto_hint_given:

        st.session_state.hint = get_hint(
            problem,
            code
        )

        st.session_state.auto_hint_given = True

if st.session_state.hint:
    st.info(st.session_state.hint)
