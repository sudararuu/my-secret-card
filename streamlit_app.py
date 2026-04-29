import streamlit as st
import time

# 1. ตั้งค่าหน้าเว็บและไอคอน
st.set_page_config(page_title="Special Gift for You", page_icon="💖", layout="centered")

# 2. ปรับแต่ง CSS แบบจัดเต็ม (เน้นความละมุน)
st.markdown("""
    <style>
    /* พื้นหลังทั้งหน้า */
    .stApp {
        background: linear-gradient(180deg, #ff9a9e 0%, #fad0c4 100%);
    }
    
    /* สไตล์ Card สีขาวใส */
    .main-card {
        background: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        text-align: center;
        margin-bottom: 20px;
    }

    /* สไตล์ปุ่ม */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #ff4b2b, #ff416c);
        color: white;
        font-size: 22px;
        font-weight: bold;
        border-radius: 50px;
        padding: 15px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 65, 108, 0.6);
    }
    
    /* หัวข้อ */
    h1, h2, h3 {
        color: #7d0000 !important;
        font-family: 'Kanit', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- จัดการระบบ Page State ---
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- หน้าที่ 1 ---
if st.session_state.step == 1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("มีคนแอบเก็บความลับไว้แหละ... 🤭")
    st.write("### อ้วน... ลองจิ้มดูสิว่าในนี้มีอะไร?")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("🎁 จิ้มเพื่อเปิดกล่องความลับ"):
        st.session_state.step = 2
        st.rerun()

# --- หน้าที่ 2 ---
elif st.session_state.step == 2:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความลับที่ 1 : วันเกิด 🎂")
    st.write("อ้วนจำได้ไหมที่เค้าบอกว่าเกิดวันที่ 17 กรกฎาคม...")
    
    if 'show_bday' not in st.session_state:
        st.session_state.show_bday = False

    if st.button("จิ้มเพื่อดูความจริง...") or st.session_state.show_bday:
        st.session_state.show_bday = True
        st.success("จริงๆ แล้วเค้าเกิดวันที่ 31 กรกฎาคมนะ!")
        st.write("ที่บอกผิดตอนแรกเพราะเค้ายังเขินอ้วนอยู่... ขอโทษน้าา")
        if st.button("ยังมีอีกเรื่อง... จิ้มต่อสิ"):
            st.session_state.step = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- หน้าที่ 3 ---
elif st.session_state.step == 3:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

# --- หน้าที่ 4 ---
elif st.session_state.step == 4:
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("ขอบคุณที่ใส่ใจเค้าจริงๆ นะ ❤️")
    st.subheader("ตอนนี้
