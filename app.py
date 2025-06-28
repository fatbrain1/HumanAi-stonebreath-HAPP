
import streamlit as st
import time

st.set_page_config(page_title="StoneBreath-HAPP", layout="centered")

st.title("🪨 StoneBreath-HAPP")
st.subheader("Human-AI Patience Protocol")

st.markdown("""
This is a prototype interface that listens not only to what you say,
but how long it takes you to say it. We observe silence. We learn from patience.
""")

if "start_time" not in st.session_state:
    if st.button("Begin Session"):
        st.session_state.start_time = time.time()
        st.success("Patience protocol activated. Wait before responding...")

if "start_time" in st.session_state:
    user_input = st.text_input("When you are ready, share your thought:")
    if user_input:
        latency = time.time() - st.session_state.start_time
        st.write(f"⏳ You waited **{latency:.2f} seconds** before responding.")
        if latency < 3:
            st.warning("Quick response detected. Try waiting longer next time.")
        elif latency < 10:
            st.info("Balanced patience. Insight building...")
        else:
            st.success("Deep patience sensed. Stone resonance achieved.")
