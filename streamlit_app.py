import streamlit as st
import time
import random

st.set_page_config(page_title="Special Gift", page_icon="💖")

# CSS ตกแต่งและฟอนต์
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Itim&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Itim', cursive !important;
        background: linear-gradient(180deg, #ff9a9e 0%, #fad0c4 100%);
        display: flex; justify-content: center; align-items: center;
    }
    
    .block-container {
        display: flex; justify-content: center; align-items: center; text-align: center;
    }

    .main-card {
        background: rgba(255, 255, 255, 0.85);
        padding: 40px; border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        max-width: 450px; width: 100%; margin: auto;
    }

    /* สไตล์ปุ่มทั่วไป */
    .stButton>button {
        width: 100%; background: #ff4b4b; color: white;
        border-radius: 50px; padding: 12px; font-size: 22px; 
        border: none; font-family: 'Itim', cursive !important;
    }

    h1, h2, h3, p, span { 
        color: #7d0000 !important; 
        text-align: center;
        font-family: 'Itim', cursive !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ระบบจำหน้าและตำแหน่งปุ่ม
if 'step' not in st.session_state: st.session_state.step = 1
if 'btn_pos' not in st.session_state: st.session_state.btn_pos = "left"
if 'move_count' not in st.session_state: st.session_state.move_count = 0

# หน้า 1: เริ่มต้น
if st.session_state.step == 1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("มีของขวัญส่งมาแหละ... 🎁")
    st.write("### อ้วน... ลองจิ้มดูสิว่าข้างในมีอะไร?")
    if st.button("จิ้มเพื่อเปิดกล่อง"):
        with st.spinner('กำลังเปิดกล่อง...'): time.sleep(1.5)
        st.session_state.step = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 2: วันเกิด
elif st.session_state.step == 2:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความลับที่ 1 : วันเกิด 🎂")
    st.write("จริงๆ แล้วเค้าเกิดวันที่ 31 กรกฎาคมนะ!")
    st.info("เค้าตั้งใจจะบอกอ้วนตั้งนานแล้ว แต่เค้าเขิน...")
    if st.button("ยังมีอีกเรื่อง... จิ้มต่อสิ"):
        st.session_state.step = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 3: ชื่อจริง
elif st.session_state.step == 3:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความลับที่ 2 : ชื่อ 📛")
    st.write("เค้าชื่อ 'สุดา' หรือ 'น้ำหวาน' นะจ๊ะ")
    st.write("เค้ากลัวอ้วนโกรธมากกกก เลยไม่กล้าบอกซักที")
    if st.button("หน้าสุดท้าย... อ้วนจิ้มสิ"):
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 4: วัดใจ (โกรธ/ไม่โกรธ)
elif st.session_state.step == 4:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("อ้วนโกรธเค้าไหม? 🥺")
    st.write("บอกความจริงมาเลย... เค้าเตรียมใจมาแล้ว")
    
    col1, col2 = st.columns(2)
    
    # สลับตำแหน่งปุ่ม "โกรธ" ไปมา
    if st.session_state.btn_pos == "left":
        with col1:
            if st.button("โกรธ! 😡"):
                st.session_state.btn_pos = "right"
                st.session_state.move_count += 1
                st.rerun()
        with col2:
            if st.button("ไม่โกรธหรอก ❤️"):
                st.session_state.step = 5
                st.rerun()
    else:
        with col1:
            if st.button("ไม่โกรธหรอก ❤️"):
                st.session_state.step = 5
                st.rerun()
        with col2:
            if st.button("โกรธ! 😡"):
                st.session_state.btn_pos = "left"
                st.session_state.move_count += 1
                st.rerun()
