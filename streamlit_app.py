import streamlit as st
import io
import contextlib

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

if st.session_state.hint:
    st.info(st.session_state.hint)


IDLE_LIMIT = 30
