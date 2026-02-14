import streamlit as st
import random

# -------- WORD LIST --------
words = ["python", "computer", "security", "network", "program"]

# -------- RESET GAME FUNCTION --------
def reset_game():
    st.session_state.word = random.choice(words)
    st.session_state.guessed = []
    st.session_state.attempts = 6
    st.session_state.status = "playing"
    st.session_state.letter = ""

# -------- INITIAL STATE --------
if "status" not in st.session_state:
    reset_game()

st.title("TASK 1 : Hangman Game")

# -------- POPUPS --------
@st.dialog("🎉 Game Won")
def win_popup():
    st.success("Congratulations! You guessed the word correctly.")
    st.write(f"Word: **{st.session_state.word}**")
    st.session_state.status = "finished"

@st.dialog("❌ Game Over")
def lose_popup():
    st.error("No attempts left!")
    st.write(f"The correct word was: **{st.session_state.word}**")
    st.session_state.status = "finished"

# -------- MAIN GAME --------
if st.session_state.status == "playing":

    word = st.session_state.word
    guessed = st.session_state.guessed

    display = " ".join(
        ch if ch in guessed else "_" for ch in word
    )

    st.write("### Word")
    st.write(display)
    st.write("Attempts Left:", st.session_state.attempts)
    st.write("Guessed Letters:", " ".join(guessed))

    def process_guess():
        letter = st.session_state.letter.lower()
        st.session_state.letter = ""

        # Allow only alphabets
        if not letter.isalpha():
            st.warning("⚠ Please enter only alphabet letters (A-Z).")
            return

        # Prevent duplicate guess
        if letter in guessed:
            st.warning("⚠ You already guessed this letter.")
            return

        guessed.append(letter)

        if letter not in word:
            st.session_state.attempts -= 1

        if all(l in guessed for l in word):
            win_popup()
        elif st.session_state.attempts == 0:
            lose_popup()

    st.text_input(
        "Enter a letter:",
        max_chars=1,
        key="letter",
        on_change=process_guess
    )

else:
    st.write("### Game Finished")
    st.write("Click below to start a new game.")

    if st.button("🔁 Restart Game"):
        reset_game()
        st.rerun()
