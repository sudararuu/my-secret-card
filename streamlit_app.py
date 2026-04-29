import streamlit as st
import time
import random

# --- 1. ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="Special Gift for You", page_icon="💖")

# --- 2. ตกแต่ง CSS (ฟอนต์ Itim + จัดกึ่งกลาง + พื้นหลัง Gradient) ---
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

# --- 3. ระบบจัดการสถานะ (Session State) ---
if 'step' not in st.session_state: st.session_state.step = 0
if 'move_count' not in st.session_state: st.session_state.move_count = 0
if 'btn_order' not in st.session_state: st.session_state.btn_order = [1, 2] # 1=โกรธ, 2=ไม่โกรธ

# --- 4. เนื้อหาแต่ละหน้า ---

# หน้า 0: หน้าปกกล่องของขวัญ
if st.session_state.step == 0:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("มีของขวัญมาส่งจ้า... 🎁")
    st.write("### อ้วน... ลองจิ้มเปิดดูหน่อยสิว่าข้างในมีอะไร?")
    if st.button("🎁 จิ้มเพื่อเปิดกล่อง"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 1: หัวข้อความลับที่ 1
elif st.session_state.step == 1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("สิ่งที่เค้าอยากบอกเรื่องวันเกิด🎂")
    st.write("เรื่องวันเกิดที่เค้าเคยบอกอ้วนไป...")
    if st.button("กดเพื่อดูความจริง"):
        with st.spinner('กำลังเปิดเผยความลับ...'): time.sleep(1.2)
        st.session_state.step = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 2: เฉลยความลับที่ 1
elif st.session_state.step == 2:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("เฉลยความจริง🥹")
    st.success("จริงๆ แล้วเค้าเกิดวันที่ 31 กรกฎาคม 🥹")
    st.write("เค้าตั้งใจจะบอกอ้วนตั้งนานแล้ว แต่เค้าปล่อยเลยมา😢...")
    if st.button("อันต่อไปอยากจะบอกอ้วนอีก"):
        st.session_state.step = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 3: หัวข้อความลับที่ 2
elif st.session_state.step == 3:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("อีกอันที่เค้ารู้สึกผิดมาตลอด จะร้องไห้ 😭")
    st.write("เรื่องชื่อ 'รวี' ที่อ้วนเรียกมาตลอด...")
    if st.button("กดได้เยย ทำใจแล้ว"):
        with st.spinner('กำลังพิมพ์ชื่อ...'): time.sleep(1.2)
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 4: เฉลยความลับที่ 2
elif st.session_state.step == 4:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("อ้วนโกรธแน่เลย 😢😢")
    st.warning("จริงๆ เค้าชื่อ 'สุดา' หรืออ้วนอยากเรียก 'น้ำหวาน'ก็ได้")
    st.write("อ้วนโกรธแน่เลยย 🥹🥹 ขอโทษนะที่เค้าโกหก")
    st.write("แต่ตอนนี้เค้าอยากจริงใจกับอ้วนที่สุดแล้วนะ")
    if st.button("ไปหน้าสุดท้ายแล้ว..."):
        st.session_state.step = 5
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 5: วัดใจ (ปุ่มวิ่งหนี + มัดมือชก)
elif st.session_state.step == 5:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("อ้วนโกรธเค้าไหม? 🥺")
    
    if st.session_state.move_count < 3:
        st.write("ตอบตามตรงเลยนะ... เค้าเตรียมใจมาแล้ว")
        col1, col2 = st.columns(2)
        
        # ระบบสุ่มตำแหน่งปุ่มโกรธ
        if st.session_state.btn_order[0] == 1:
            with col1:
                if st.button("โกรธ! 😡"):
                    st.session_state.move_count += 1
                    random.shuffle(st.session_state.btn_order)
                    st.rerun()
            with col2:
                if st.button("ไม่โกรธ ❤️"):
                    st.session_state.step = 6
                    st.rerun()
        else:
            with col1:
                if st.button("ไม่โกรธ ❤️"):
                    st.session_state.step = 6
                    st.rerun()
            with col2:
                if st.button("โกรธ! 😡"):
                    st.session_state.move_count += 1
                    random.shuffle(st.session_state.btn_order)
                    st.rerun()
    else:
        # ด่านสุดท้าย: ปุ่มโกรธหายไป เหลือแต่ปุ่มไม่โกรธ 3 ปุ่มรัวๆ
        st.write("โถ่... ปุ่มโกรธมันพังไปแล้วอ้วน")
        st.write("### อ้วนยังจะโกรธเค้าลงจริงๆ หรอ? 🥺")
        if st.button("ไม่โกรธ ❤️"): st.session_state.step = 6; st.rerun()
        if st.button("ไม่โกรธหรอกเจ้าไดโน 🦖"): st.session_state.step = 6; st.rerun()
        if st.button("ไม่โกรธแล้วจ้าาา ❤️"): st.session_state.step = 6; st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 6: หน้าจบ (สารภาพรัก + เพลง)
elif st.session_state.step == 6:
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("รักอ้วนที่สุดเลย! ❤️")
    st.subheader("ขอบคุณที่ไม่โกรธน้ำหวานน้าา 🥹🥹")
    st.write("ขอบคุณที่ใส่ใจและรับฟังความจริงของเค้านะ")
    st.write("---")
    st.markdown("""
        <p style="font-size:18px;">🎵 เพลงนี้... เค้าอยากให้เราฟังด้วยกันนะ</p>
        <a href="https://www.youtube.com/watch?v=kYI4M8a9F0g" target="_blank" style="text-decoration:none;">
            <div style="background: #ff4b4b; color:white; padding:15px; border-radius:50px; font-weight:bold; font-size:22px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                ▶️ ฟังเพลง 'ข้างกัน'
            </div>
        </a>
        <br>
    """, unsafe_allow_html=True)
    if st.button("เริ่มต้นใหม่ (ขอโทษงับ เค้ารู้สึกผิดจริง ๆ 
😭🥹)"):
        for key in st.session_state.keys(): del st.session_state[key]
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
