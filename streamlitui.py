import streamlit as st
import random

st.set_page_config(page_title="Guess Game", page_icon="🎯")

st.title("🎯 Guess Comp vs Golu")
st.write("Enter number (1–100)")

# state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.win = False

guess = st.text_input("Your Guess", placeholder="Type number here")

if st.button("🎯 Check"):
    if not guess.isdigit():
        st.error("Enter number only")
    else:
        guess = int(guess)
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.info("⬇️ Too Low")
        elif guess > st.session_state.number:
            st.info("⬆️ Too High")
        else:
            st.success("🏆 Golu Won!")
            st.write("Attempts:", st.session_state.attempts)
            st.balloons()
            st.audio(
                "https://www.soundjay.com/buttons/sounds/button-3.mp3",
                autoplay=True
            )
            st.session_state.win = True

if st.session_state.win:
    if st.button("🔄 Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.win = False


