import streamlit as st

# Encryption and Decryption Functions
def julie_encrypt(word):
    square_length = len(word) ** 2
    encrypted_word = ""
    for char in word:
        # Encrypt each character by modifying its ASCII value
        new_ascii = ord(char) + square_length
        encrypted_word += chr(new_ascii)
    return encrypted_word

def julie_decrypt(word):
    # The word length must match the original encrypted word length for accurate decryption
    square_length = len(word) ** 2
    decrypted_word = ""
    for char in word:
        # Decrypt by reversing the encryption logic
        new_ascii = ord(char) - square_length
        decrypted_word += chr(new_ascii)
    return decrypted_word

# Set up the page configuration
st.set_page_config(page_title="Crypto Quadratic Defender", page_icon="🔐", layout="centered")

# Add background video and styling
st.markdown("""
    <style>
        body {
            background: url('https://pixabay.com/videos/download/video-204306_small.mp4') no-repeat center center fixed;
            background-size: cover;
        }
        .small-text {
            font-size: 12px;
            text-align: center;
            color: white;
        }
        .main-text {
            text-align: center;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# App Title
st.markdown("<h1 class='main-text'>Crypto Quadratic Defender</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='main-text'>Encrypt and Decrypt Messages with a Quadratic Twist!</h3>", unsafe_allow_html=True)

# Choose between Encrypt or Decrypt
operation = st.radio("Choose an operation", ["Encrypt", "Decrypt"])

# Input and processing based on the operation
if operation == "Encrypt":
    st.subheader("Encrypt Your Text")
    original_word = st.text_area("Enter a word or phrase to encrypt:", height=100).upper()

    if original_word:
        encrypted_word = julie_encrypt(original_word)
        st.markdown(f"### **Encrypted Word:** `{encrypted_word}`")

elif operation == "Decrypt":
    st.subheader("Decrypt Your Text")
    encrypted_word = st.text_area("Enter the encrypted word or phrase:", height=100).upper()

    if encrypted_word:
        # Decrypt only if the encrypted word has content
        if encrypted_word:
            try:
                decrypted_word = julie_decrypt(encrypted_word)
                st.markdown(f"### **Decrypted Word:** `{decrypted_word}`")
            except Exception as e:
                st.error(f"Error during decryption: {str(e)}")

# Credits and copyright
st.markdown("<br><p class='small-text'>**CREDITS: Hariharan M** | COPYRIGHT 2024 | 2011.HARIHARAN@GMAIL.COM</p>", unsafe_allow_html=True)
