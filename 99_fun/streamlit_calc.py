import streamlit as st

st.set_page_config(page_title="Streamlit 웹 계산기", page_icon="🧮", layout="centered")

st.title("🧮 파이썬 Streamlit 웹 계산기")

if 'expr' not in st.session_state:
    st.session_state.expr = ""

st.text_input("계산 수식 / 결과", value=st.session_state.expr, key="display", disabled=True)

col1, col2, col3, col4 = st.columns(4)

def press(val):
    st.session_state.expr += str(val)

def clear():
    st.session_state.expr = ""

def calc():
    try:
        st.session_state.expr = str(eval(st.session_state.expr))
    except Exception:
        st.session_state.expr = "Error"

with col1:
    if st.button("C", use_container_width=True): clear()
    if st.button("7", use_container_width=True): press("7")
    if st.button("4", use_container_width=True): press("4")
    if st.button("1", use_container_width=True): press("1")
    if st.button("0", use_container_width=True): press("0")

with col2:
    if st.button("(", use_container_width=True): press("(")
    if st.button("8", use_container_width=True): press("8")
    if st.button("5", use_container_width=True): press("5")
    if st.button("2", use_container_width=True): press("2")
    if st.button(".", use_container_width=True): press(".")

with col3:
    if st.button(")", use_container_width=True): press(")")
    if st.button("9", use_container_width=True): press("9")
    if st.button("6", use_container_width=True): press("6")
    if st.button("3", use_container_width=True): press("3")
    if st.button("=", use_container_width=True): calc()

with col4:
    if st.button("/", use_container_width=True): press("/")
    if st.button("*", use_container_width=True): press("*")
    if st.button("-", use_container_width=True): press("-")
    if st.button("+", use_container_width=True): press("+")
