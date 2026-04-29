import streamlit as st
import time
import random

# --- 1. ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="Sweet Secret for You", page_icon="🦖")

# --- 2. ตกแต่ง CSS (Earth Tone + มินิมอลการ์ด) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Itim&display=swap');
    
    /* พื้นหลังโทนเอิร์ธโทน (Creamy Beige) */
    html, body, [class*="css"], .stApp {
        font-family: 'Itim', cursive !important;
        background-color: #F5EBE0 !important; 
        display: flex; justify-content: center; align-items: center;
    }
    
    /* กรอบ (Card) สีขาวมินิมอล */
    .main-card {
        background: #FFFFFF;
        padding: 40px; 
        border-radius: 25px;
        border: 2px solid #D5BDAF; /* ขอบสีน้ำตาลอ่อน */
        box-shadow: 0 10px 25px rgba(165, 148, 116, 0.2);
        max-width: 450px; 
        width: 100%; 
        margin: auto;
        text-align: center;
    }

    /* ตกแต่งรูปภาพ */
    .stImage > img {
        border-radius: 15px;
        margin-bottom: 20px;
    }

    /* ปุ่มกดสีส้มอิฐ/น้ำตาลอุ่นๆ */
    .stButton>button {
        width: 100%; 
        background: #D69F7E; 
        color: white;
        border-radius: 12px; 
        padding: 10px; 
        font-size: 20px; 
        border: none; 
        font-family: 'Itim', cursive !important;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background: #BC8A5F;
        transform: translateY(-2px);
    }

    /* สีตัวอักษรโทนเข้มแต่ซอฟต์ */
    h1, h2, h3, p, span { 
        color: #6D4C41 !important; 
        text-align: center; 
        font-family: 'Itim', cursive !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ระบบจัดการสถานะ ---
if 'step' not in st.session_state: st.session_state.step = 0
if 'move_count' not in st.session_state: st.session_state.move_count = 0
if 'btn_order' not in st.session_state: st.session_state.btn_order = [1, 2]

# --- 4. เนื้อหาแต่ละหน้า ---

# หน้า 0: เริ่มต้น
if st.session_state.step == 0:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # ไดโนมินิมอล
    st.title("มีของขวัญมาส่งงับ... 🎁")
    st.write("อ้วน... ลองจิ้มเปิดดูหน่อยสิ")
    if st.button("เปิดกล่องของขวัญ"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 1: ความลับที่ 1
elif st.session_state.step == 1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("เค้ามีเรื่องจะบอก 🎂")
    st.write("เรื่องวันเกิดที่เค้าเคยบอกอ้วนไป...")
    if st.button("เฉลยความจริง"):
        with st.spinner('แป๊บนึงนะ...'): time.sleep(1)
        st.session_state.step = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 2: เฉลยความลับที่ 1
elif st.session_state.step == 2:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("ความจริงเปิดเผย")
    st.write("จริงๆ เค้าเกิดวันที่ **31 กรกฎาคม** 😢😢")
    st.write("ขอโทษนะที่โกหกอ้วน ปล่อยเลยตามเลยมาตลอด เค้าขอโทษ")
    if st.button("มีอีกอย่าง เค้ากลัวอ้วนโกรธมาก ๆ ..."):
        st.session_state.step = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 3: ความลับที่ 2
elif st.session_state.step == 3:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("อ้วนนน เค้าขอโทษ🥺")
    st.write("เรื่องชื่อ 'รวี' ที่อ้วนเรียกมาตลอด...")
    if st.button("ชื่อจริงๆ ของเค้าคือ"):
        with st.spinner('กำลังพิมพ์ชื่อ...'): time.sleep(1)
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 4: เฉลยความลับที่ 2
elif st.session_state.step == 4:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("🥺🥺🥺")
    st.warning("เค้าชื่อ 'สุดา' หรืออ้วนจะเรียกหวานก็ได้ 😢")
    st.write("กลัวอ้วนโกรธ เลยไม่กล้าบอกซักที")
    st.write("แต่ตอนนี้อยากจริงใจที่สุดแล้ว")
    if st.button("หน้าสุดท้าย😢..."):
        st.session_state.step = 5
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 5: วัดใจ (ปุ่มวิ่งหนี -> 3 ปุ่มมัดมือชก)
elif st.session_state.step == 5:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("อ้วนโกรธเค้าไหม? 🥺")
    
    if st.session_state.move_count < 3:
        st.write("อย่าโกรธเค้าเลยนะ...")
        col1, col2 = st.columns(2)
        if st.session_state.btn_order[0] == 1:
            with col1:
                if st.button("โกรธ! 😡"):
                    st.session_state.move_count += 1
                    random.shuffle(st.session_state.btn_order)
                    st.rerun()
            with col2:
                if st.button("ไม่โกรธ ❤️"): st.session_state.step = 6; st.rerun()
        else:
            with col1:
                if st.button("ไม่โกรธ ❤️"): st.session_state.step = 6; st.rerun()
            with col2:
                if st.button("โกรธ! 😡"):
                    st.session_state.move_count += 1
                    random.shuffle(st.session_state.btn_order)
                    st.rerun()
    else:
        # จุดพีค: ปุ่มโกรธพัง เหลือแต่ไม่โกรธ 3 ปุ่มรัวๆ
        st.write("โถ่... ปุ่มโกรธมันพังไปแล้ว")
        st.write("### อ้วนจะโกรธเค้าจริงๆ หรอ? 🥺")
        if st.button("ไม่โกรธ❤️"): st.session_state.step = 6; st.rerun()
        if st.button("ไม่โกรธ 🦕"): st.session_state.step = 6; st.rerun()
        if st.button("เค้าไม่ให้โกรธ 🐱"): st.session_state.step = 6; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# หน้า 6: บทสรุป (เพลง + หัวใจ)
elif st.session_state.step == 6:
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/cute-dino-hugging-cat-cartoon_23-2148154130.jpg", width=200) # รูปคู่น่ารักๆ
    st.title("ขอโทษนะอ้วนนน😭😭")
    st.write("ยกโทษให้เค้าได้มั้ยย 🥺🥺")
    st.write("---")
    st.markdown("""
        <a href="https://www.youtube.com/watch?v=kYI4M8a9F0g" target="_blank" style="text-decoration:none;">
            <div style="background: #D69F7E; color:white; padding:15px; border-radius:12px; font-weight:bold; font-size:20px;">
                ▶️ ฟังเพลงของเรากันนะ
            </div>
        </a>
    """, unsafe_allow_html=True)
    if st.button("กลับหน้าแรก"):
        for key in st.session_state.keys(): del st.session_state[key]
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
