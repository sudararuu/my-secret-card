import streamlit as st
import time

st.set_page_config(page_title="Secret of Namwan", page_icon="🍯")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #ffb7b7;
        color: #7d0000;
        font-size: 20px;
        border-radius: 50px;
        padding: 20px;
        border: 2px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    st.title("มีคนแอบเก็บความลับไว้แหละ... 🤭")
    st.write("### อ้วน... ลองจิ้มดูสิว่าในนี้มีอะไร?")
    if st.button("🎁 จิ้มเพื่อเปิดกล่องความลับ"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.header("ความลับที่ 1 : วันเกิด 🎂")
    st.write("อ้วนจำได้ไหมที่เค้าบอกว่าเกิดวันที่ 17 กรกฎาคม...")
    if st.button("จิ้มเพื่อดูความจริง..."):
        with st.spinner("กำลังรวบรวมความกล้า..."):
            time.sleep(1.5)
        st.success("จริงๆ แล้วเค้าเกิดวันที่ 31 กรกฎาคมนะ!")
        if st.button("ยังมีอีกเรื่อง... จิ้มต่อสิ"):
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    st.header("ความลับที่ 2 : ชื่อ 📛")
    st.write("ชื่อ 'รวี' ที่อ้วนเรียกมาตลอดน่ะ...")
    if st.button("จิ้มเพื่อฟังชื่อจริงๆ ของเค้า"):
        st.warning("จริงๆ เค้าชื่อ 'สุดา' หรือจะเรียก 'น้ำหวาน' ก็ได้นะ")
        st.write("ชื่อน้ำหวาน... หวานเหมือนความรักที่เค้ามีให้อ้วนเลยนะ")
        if st.button("จิ้มหน้าสุดท้าย... เพื่อฟังเพลงของเรา"):
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.title("ขอบคุณที่ใส่ใจเค้าจริงๆ นะ ❤️")
    st.subheader("ตอนนี้ไม่มีความลับต่อกันแล้ว... รักอ้วนที่สุดเยย")
    st.write("---")
    st.write("### 🎵 อยู่ข้างกันไปนานๆ นะ")
    st.video("https://www.youtube.com/watch?v=kYI4M8a9F0g")
    
    if st.button("กลับไปหน้าแรก"):
        st.session_state.step = 1
        st.rerun()
