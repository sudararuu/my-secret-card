import streamlit as st
import time

st.set_page_config(page_title="Special Gift", page_icon="💖")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #ff9a9e 0%, #fad0c4 100%); }
    .main-card { background: rgba(255, 255, 255, 0.85); padding: 30px; border-radius: 30px; text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,0.1); }
    .stButton>button { width: 100%; background: #ff4b4b; color: white; border-radius: 50px; padding: 15px; font-size: 20px; border: none; }
    h1, h2, h3 { color: #7d0000 !important; }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("มีคนแอบเก็บความลับไว้แหละ... 🤭")
    st.write("### อ้วน... ลองจิ้มดูสิว่าในนี้มีอะไร?")
    if st.button("🎁 จิ้มเพื่อเปิดกล่องความลับ"):
        st.session_state.step = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 2:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความลับที่ 1 : วันเกิด 🎂")
    st.write("จริงๆ แล้วเค้าเกิดวันที่ 31 กรกฎาคมนะ!")
    if st.button("ยังมีอีกเรื่อง... จิ้มต่อสิ"):
        st.session_state.step = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 3:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความลับที่ 2 : ชื่อ 📛")
    st.write("เค้าชื่อ 'สุดา' หรือจะเรียก 'น้ำหวาน' ก็ได้นะ")
    if st.button("จิ้มหน้าสุดท้าย... เพื่อฟังเพลงของเรา"):
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 4:
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("รักอ้วนที่สุดเยยนะ ❤️")
    st.write("---")
    st.markdown("""
        <a href="https://www.youtube.com/watch?v=kYI4M8a9F0g" target="_blank" style="text-decoration:none;">
            <div style="background: #ff4b4b; color:white; padding:15px; border-radius:50px; font-weight:bold; font-size:20px;">
                ▶️ ฟังเพลง 'ข้างกัน'
            </div>
        </a>
    """, unsafe_allow_html=True)
    if st.button("เริ่มต้นใหม่"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
