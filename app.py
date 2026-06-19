import streamlit as st

st.title("Python学習支援システム")

problem = st.text_area(
    "問題文",
    height=200
)

code = st.text_area(
    "コード",
    height=300
)

from streamlit_ace import st_ace

code = st_ace(
    language="python",
    theme="github",
    height=400
)

from ai_hint import get_hint

if st.button("ヒントをもらう"):
    #hint = get_hint(problem, code)

    st.write(hint)

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
if idle_time > IDLE_LIMIT:

    st.warning(
        "悩んでいる？ヒントをあげるよ"
    )

    hint = get_hint(
        problem,
        code
    )

    #st.info(hint)