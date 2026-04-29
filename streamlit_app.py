import streamlit as st
import time
import random

st.set_page_config(page_title="Special Gift", page_icon="💖")

# CSS ตกแต่ง จัดกึ่งกลาง และฟอนต์น่ารักๆ
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

# ระบบจำสถานะ
if 'step' not in st.session_state: st.session_state.step = 1
if 'move_count' not in st.session_state: st.session_state.move_count = 0
if 'btn_order' not in st.session_state: st.session_state.btn_order = [1, 2] # 1=โกรธ, 2=ไม่โกรธ

# หน้า 1: เริ่มต้น
if st.session_state.step == 1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("มีของขวัญมาส่งจ้า... 🎁")
    st.write("### อ้วน... ลองจิ้มเปิดดูหน่อยสิ")
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
    st.write("เค้าตั้งใจจะบอกอ้วนตั้งนานแล้ว แต่เค้ากลัวอ้วนโกรธเค้า🥹...")
    if st.button("ยังมีอีกเรื่อง... จิ้มต่อสิ"):
        st.session_state.step = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 3: ชื่อจริง
elif st.session_state.step == 3:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความลับที่ 2 : ชื่อ 📛")
    st.write("เค้าชื่อ 'น้ำหวาน' นะ (หรือจะเรียกสุดาก็ได้)")
    st.write("เค้ากลัวอ้วนโกรธ เลยไม่กล้าบอกซักที")
    if st.button("หน้าสุดท้าย... อ้วนจิ้มสิ"):
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 4: วัดใจ (ปุ่มวิ่งหนี)
elif st.session_state.step == 4:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("อ้วนโกรธเค้าไหม? 🥺")
    
    # ถ้ากดโกรธครบ 3 ครั้ง ปุ่มโกรธจะหายไปเลย!
    if st.session_state.move_count < 3:
        st.write("จิ้มบอกความจริงมาเลย...")
        
        # สุ่มลำดับปุ่มใหม่ทุกครั้งที่กดโกรธ
        col1, col2 = st.columns(2)
        buttons = []
        
        if st.session_state.btn_order[0] == 1:
            with col1:
                if st.button("โกรธ! 😡"):
                    st.session_state.move_count += 1
                    random.shuffle(st.session_state.btn_order) # สลับตำแหน่ง
                    st.rerun()
            with col2:
                if st.button("ไม่โกรธ ❤️"):
                    st.session_state.step = 5
                    st.rerun()
        else:
            with col1:
                if st.button("ไม่โกรธ ❤️"):
                    st.session_state.step = 5
                    st.rerun()
            with col2:
                if st.button("โกรธ! 😡"):
                    st.session_state.move_count += 1
                    random.shuffle(st.session_state.btn_order) # สลับตำแหน่ง
                    st.rerun()
    else:
        # บังคับไม่ให้โกรธแล้ว
        st.write("โถ่... ปุ่มโกรธมันพังไปแล้วอ้วน")
        st.write("แสดงว่าอ้วนโกรธเค้าไม่ลงหรอก จิ้มปุ่มข้างล่างเถอะ ✨")
        if st.button("ยอมก็ได้ ไม่โกรธแล้ว ❤️"):
            st.session_state.step = 5
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 5: บทสรุป
elif st.session_state.step == 5:
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("รักอ้วนที่สุดในโลกเยย! ❤️")
    st.subheader("ขอบคุณที่ไม่โกรธน้ำหวานนะ")
    st.write("---")
    st.markdown("""
        <a href="https://www.youtube.com/watch?v=kYI4M8a9F0g" target="_blank" style="text-decoration:none;">
            <div style="background: #ff4b4b; color:white; padding:15px; border-radius:50px; font-weight:bold; font-size:22px;">
                ▶️ ฟังเพลงของเรากัน
            </div>
        </a>
    """, unsafe_allow_html=True)
    if st.button("กลับไปหน้าแรก"):
        for key in st.session_state.keys(): del st.session_state[key]
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
