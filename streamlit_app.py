import streamlit as st
import time

st.set_page_config(page_title="Secret of Namwan", page_icon="🍯")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #ffb7b7;
        color: #7d0000;
        font-size: 20px;
        border-radius: 50px;
        padding: 15px;
        border: 2px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 1

# หน้า 1: เริ่มต้น
if st.session_state.step == 1:
    st.title("มีคนแอบเก็บความลับไว้แหละ... 🤭")
    st.write("### อ้วน... ลองจิ้มดูสิว่าในนี้มีอะไร?")
    if st.button("🎁 จิ้มเพื่อเปิดกล่องความลับ"):
        st.session_state.step = 2
        st.rerun()

# หน้า 2: สารภาพวันเกิด
elif st.session_state.step == 2:
    st.header("ความลับที่ 1 : วันเกิด 🎂")
    st.write("อ้วนจำได้ไหมที่เค้าบอกว่าเกิดวันที่ 17 กรกฎาคม...")
    
    if 'show_bday' not in st.session_state:
        st.session_state.show_bday = False

    if st.button("จิ้มเพื่อดูความจริง...") or st.session_state.show_bday:
        st.session_state.show_bday = True
        st.success("จริงๆ แล้วเค้าเกิดวันที่ 31 กรกฎาคมนะ!")
        if st.button("ยังมีอีกเรื่อง... จิ้มต่อสิ"):
            st.session_state.step = 3
            st.rerun()

# หน้า 3: สารภาพชื่อ
elif st.session_state.step == 3:
    st.header("ความลับที่ 2 : ชื่อ 📛")
    st.write("ชื่อ 'รวี' ที่อ้วนเรียกมาตลอดน่ะ...")
    
    if 'show_name' not in st.session_state:
        st.session_state.show_name = False

    if st.button("จิ้มเพื่อฟังชื่อจริงๆ ของเค้า") or st.session_state.show_name:
        st.session_state.show_name = True
        st.warning("จริงๆ เค้าชื่อ 'สุดา' หรือจะเรียก 'น้ำหวาน' ก็ได้นะ")
        st.write("ชื่อน้ำหวาน... หวานเหมือนความรักที่เค้ามีให้อ้วนเลยนะ")
        if st.button("จิ้มหน้าสุดท้าย... เพื่อฟังเพลงของเรา"):
            st.session_state.step = 4
            st.rerun()

# หน้า 4: บทสรุป
elif st.session_state.step == 4:
    st.balloons()
    st.title("ขอบคุณที่ใส่ใจเค้าจริงๆ นะ ❤️")
    st.subheader("ตอนนี้ไม่มีความลับต่อกันแล้ว... รักอ้วนที่สุดเยย")
    st.write("---")
    st.write("### 🎵 อยู่ข้างกันไปนานๆ นะ")
    st.video("https://www.youtube.com/watch?v=kYI4M8a9F0g")
    
    if st.button("กลับไปหน้าแรก"):
        st.session_state.step = 1
        st.session_state.show_bday = False
        st.session_state.show_name = False
        st.rerun()
