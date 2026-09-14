import os
import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox


# ---------------------------------------------------------
# 1. PyQt6 데스크톱 앱 실행 함수
# ---------------------------------------------------------
def run_pyqt_app():
    from PyQt6.QtCore import Qt
    from PyQt6.QtWidgets import (
        QApplication,
        QGridLayout,
        QLineEdit,
        QPushButton,
        QVBoxLayout,
        QWidget,
    )

    class PyQtCalculator(QWidget):
        def __init__(self):
            super().__init__()
            self.expression = ""
            self.init_ui()

        def init_ui(self):
            self.setWindowTitle("PyQt6 전문 데스크톱 계산기")
            self.setFixedSize(320, 420)

            layout = QVBoxLayout()

            # 디스플레이 입력창
            self.display = QLineEdit()
            self.display.setReadOnly(True)
            self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.display.setStyleSheet(
                "font-size: 24px; padding: 10px; background-color: #f8f9fa;"
            )
            layout.addWidget(self.display)

            # 버튼 레이아웃
            grid = QGridLayout()
            buttons = [
                ("C", 0, 0),
                ("(", 0, 1),
                (")", 0, 2),
                ("/", 0, 3),
                ("7", 1, 0),
                ("8", 1, 1),
                ("9", 1, 2),
                ("*", 1, 3),
                ("4", 2, 0),
                ("5", 2, 1),
                ("6", 2, 2),
                ("-", 2, 3),
                ("1", 3, 0),
                ("2", 3, 1),
                ("3", 3, 2),
                ("+", 3, 3),
                ("0", 4, 0),
                (".", 4, 1),
                ("=", 4, 2),
            ]

            for text, row, col in buttons:
                btn = QPushButton(text)
                btn.setStyleSheet("font-size: 18px; padding: 15px;")
                if text == "=":
                    btn.clicked.connect(self.calculate)
                    grid.addWidget(btn, row, col, 1, 2)
                elif text == "C":
                    btn.clicked.connect(self.clear)
                    grid.addWidget(btn, row, col)
                else:
                    btn.clicked.connect(lambda _, t=text: self.on_click(t))
                    grid.addWidget(btn, row, col)

            layout.addLayout(grid)
            self.setLayout(layout)

        def on_click(self, char):
            self.expression += char
            self.display.setText(self.expression)

        def clear(self):
            self.expression = ""
            self.display.setText("")

        def calculate(self):
            try:
                result = str(eval(self.expression))
                self.display.setText(result)
                self.expression = result
            except Exception:
                self.display.setText("Error")
                self.expression = ""

    app = QApplication(sys.argv)
    calc = PyQtCalculator()
    calc.show()
    sys.exit(app.exec())


# ---------------------------------------------------------
# 2. Streamlit 웹 UI 실행 함수 및 웹 파일 생성
# ---------------------------------------------------------
def run_streamlit_app():
    BASE_DIR = Path(__file__).resolve().parent
    web_app_file = BASE_DIR / "streamlit_calc.py"

    # Streamlit 전용 파이썬 스크립트 임시 생성
    streamlit_code = """import streamlit as st

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
"""
    with open(web_app_file, "w", encoding="utf-8") as f:
        f.write(streamlit_code)

    print("\n[알림] 웹 브라우저에서 Streamlit 계산기를 실행합니다...")
    # 터미널 명령어로 streamlit run 실행
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(web_app_file)])


# ---------------------------------------------------------
# 3. 모드 선택 팝업 GUI (Tkinter 기반)
# ---------------------------------------------------------
def launch_selector():
    root = tk.Tk()
    root.title("실행 모드 선택")
    root.geometry("360x200")
    root.eval("tk::PlaceWindow . center")  # 화면 중앙에 팝업 배치

    label = tk.Label(
        root,
        text="어떤 실행 환경으로 계산기를 실행하시겠습니까?",
        font=("Arial", 11, "bold"),
        pady=20,
    )
    label.pack()

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    def select_desktop():
        root.destroy()
        run_pyqt_app()

    def select_web():
        root.destroy()
        run_streamlit_app()

    btn_desktop = tk.Button(
        btn_frame,
        text="🖥️ 데스크톱 앱 (PyQt6)",
        font=("Arial", 11),
        bg="#2196F3",
        fg="white",
        padx=15,
        pady=10,
        command=select_desktop,
    )
    btn_desktop.grid(row=0, column=0, padx=10)

    btn_web = tk.Button(
        btn_frame,
        text="🌐 웹 UI (Streamlit)",
        font=("Arial", 11),
        bg="#4CAF50",
        fg="white",
        padx=15,
        pady=10,
        command=select_web,
    )
    btn_web.grid(row=0, column=1, padx=10)

    root.mainloop()


if __name__ == "__main__":
    launch_selector()
