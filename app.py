import streamlit as st

st.markdown("# 앱 UI 만들기")
name = st.text_input("이름", placeholder="이름")
grade = st.radio("학년", ["1", "2", "3"], horizontal=True)
klass = st.number_input("반", value=1)
difficulty = st.select_slider("난이도",options=["낮음", "보통", "높음"])
score = st.slider("점수", 0, 100,50)
sogam = st.text_input("소감")

if st.button("확인"):
    st.success(f"{name}/{grade}학년/{klass}반/{difficulty}")
    st.markdown(f"점수:{score}")
    st.info(f"소감:{sogam}")
