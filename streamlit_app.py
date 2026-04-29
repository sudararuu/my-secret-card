import streamlit as st
import time

st.set_page_config(page_title="Special Gift", page_icon="💖")

# ดึงฟอนต์จาก Google Fonts และตั้งค่ากลางหน้าจอ
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
        max-width: 400px; width: 100%; margin: auto;
    }

    .stButton>button {
        width: 100%; background: #ff4b4b; color: white;
        border-radius: 50px; padding: 15px; font-size: 24px; 
        border: none; font-family: 'Itim', cursive !important;
    }

    h1, h2, h3, p, span { 
        color: #7d0000 !important; 
        text-align: center;
        font-family: 'Itim', cursive !important;
    }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 1

# หน้า 1: เริ่มต้น
if st.session_state.step == 1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("มีของขวัญส่งมาแหละ... 🎁")
    st.write("### อ้วน... ลองจิ้มดูสิว่าข้างในมีอะไร?")
    if st.button("จิ้มเพื่อเปิดกล่อง"):
        with st.spinner('กำลังเปิดกล่อง...'):
            time.sleep(2)
        st.session_state.step = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 2: สารภาพวันเกิด
elif st.session_state.step == 2:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความลับที่ 1 : วันเกิด 🎂")
    st.write("อ้วนจำได้ไหมที่เค้าบอกว่าเกิดวันที่ 17 กรกฎาคม...")
    if st.button("จิ้มเพื่อดูความจริง"):
        with st.spinner('กำลังรวบรวมความกล้า...'):
            time.sleep(2)
        st.session_state.is_reveal_bday = True
    
    if st.session_state.get('is_reveal_bday'):
        st.success("จริงๆ แล้วเค้าเกิดวันที่ 31 กรกฎาคมนะ!")
        if st.button("ยังมีอีกเรื่อง... จิ้มต่อสิ"):
            st.session_state.step = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 3: สารภาพชื่อ
elif st.session_state.step == 3:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความลับที่ 2 : ชื่อ 📛")
    st.write("ชื่อ 'รวี' ที่อ้วนเรียกมาตลอดน่ะ...")
    if st.button("จิ้มเพื่อฟังชื่อจริงของเค้า"):
        with st.spinner('กำลังพิมพ์ชื่อ...'):
            time.sleep(2)
        st.session_state.is_reveal_name = True
        
    if st.session_state.get('is_reveal_name'):
        st.warning("จริงๆ เค้าชื่อ 'สุดา' หรือ 'น้ำหวาน' จ้า")
        st.write("ชื่อน้ำหวาน... หวานเหมือนเค้าตอนอ้อนอ้วนเลยนะ")
        if st.button("หน้าสุดท้าย... คลิกสิ"):
            st.session_state.step = 4
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 4: บทสรุป
elif st.session_state.step == 4:
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("รักอ้วนที่สุดเยยนะ ❤️")
    st.write("---")
    st.markdown("""
        <a href="https://www.youtube.com/watch?v=kYI4M8a9F0g" target="_blank" style="text-decoration:none;">
            <div style="background: #ff4b4b; color:white; padding:15px; border-radius:50px; font-weight:bold; font-size:22px; font-family: 'Itim', cursive;">
                ▶️ ฟังเพลง 'ข้างกัน'
            </div>
        </a>
        <br>
    """, unsafe_allow_html=True)
    if st.button("กลับหน้าแรก"):
        for key in st.session_state.keys(): del st.session_state[key]
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
