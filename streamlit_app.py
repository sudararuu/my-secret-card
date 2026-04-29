import streamlit as st
import time

# --- ตั้งค่าหน้าเว็บให้ดูเป็น Card ---
st.set_page_config(page_title="Secret of Namwan", page_icon="🍯")

# ปรับแต่ง CSS ให้ปุ่มดูน่ากดและหน้าจอสวยขึ้น
st.markdown("""
    <style>
    .stButton>button {
        background-color: #ffb7b7;
        color: #7d0000;
        font-size: 20px;
        border-radius: 50px;
        padding: 20px;
        border: 2px solid #ff4b4b;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff4b4b;
        color: white;
        transform: scale(1.05);
    }
    .reportview-container {
        background: #fffafa;
    }
    </style>
    """, unsafe_all_with_logic=True)

# --- จัดการระบบการคลิก (Session State) ---
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- หน้าที่ 1: หน้าทักทาย ---
if st.session_state.step == 1:
    st.title("มีคนแอบเก็บความลับไว้แหละ... 🤭")
    st.write("### อ้วน... ลองจิ้มดูสิว่าในนี้มีอะไร?")
    if st.button("🎁 จิ้มเพื่อเปิดกล่องความลับ"):
        st.session_state.step = 2
        st.rerun()

# --- หน้าที่ 2: สารภาพวันเกิด ---
elif st.session_state.step == 2:
    st.header("ความลับที่ 1 : วันเกิด 🎂")
    st.write("อ้วนจำได้ไหมที่เค้าบอกว่าเกิดวันที่ 17 กรกฎาคม...")
    if st.button("จิ้มเพื่อดูความจริง..."):
        with st.spinner("กำลังเรียบเรียงความกล้า..."):
            time.sleep(1.5)
        st.success("จริงๆ แล้วเค้าเกิดวันที่ 31 กรกฎาคมนะ! (เค้าคือยัยธาตุไฟแหละ)")
        if st.button("ยังมีอีกเรื่อง... จิ้มต่อสิ"):
            st.session_state.step = 3
            st.rerun()

# --- หน้าที่ 3: สารภาพชื่อ ---
elif st.session_state.step == 3:
    st.header("ความลับที่ 2 : ชื่อ 📛")
    st.write("ชื่อ 'รวี' ที่อ้วนเรียกมาตลอดน่ะ...")
    if st.button("จิ้มเพื่อฟังชื่อจริงๆ ของเค้า"):
        st.warning("จริงๆ เค้าชื่อ 'สุดา' หรือจะเรียก 'น้ำหวาน' ก็ได้นะ")
        st.write("ชื่อน้ำหวาน... หวานเหมือนความรักที่เค้ามีให้อ้วนเลยนะ (งุ้ยยย)")
        if st.button("จิ้มหน้าสุดท้าย... เพื่อฟังเพลงของเรา"):
            st.session_state.step = 4
            st.rerun()

# --- หน้าที่ 4: สรุปจบหวานๆ ---
elif st.session_state.step == 4:
    st.balloons()
    st.title("ขอบคุณที่ใส่ใจเค้าจริงๆ นะ ❤️")
    st.subheader("ตอนนี้ไม่มีความลับต่อกันแล้ว... รักอ้วนที่สุดเยย")
    
    # ใส่เพลง 'ข้างกัน' ให้เขาฟัง
    st.write("---")
    st.write("### 🎵 อยู่ข้างกันไปนานๆ นะ")
    st.video("https://www.youtube.com/watch?v=kYI4M8a9F0g")
    
    if st.button("จิ้มเพื่อกลับไปหน้าแรก"):
        st.session_state.step = 1
        st.rerun()
