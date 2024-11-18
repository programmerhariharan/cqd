import streamlit as st

# Encryption and Decryption Functions
def julie_encrypt(word):
    square_length = len(word) ** 2
    encrypted_word = ""
    for char in word:
        new_ascii = ord(char) + square_length
        encrypted_word += chr(new_ascii)
    return encrypted_word

def julie_decrypt(word):
    square_length = len(word) ** 2
    decrypted_word = ""
    for char in word:
        new_ascii = ord(char) - square_length
        decrypted_word += chr(new_ascii)
    return decrypted_word

# Streamlit App UI
st.set_page_config(page_title="Crypto Quadratic Defender", page_icon="🔐", layout="centered")

# Title Section
st.title("Crypto Quadratic Defender")
st.markdown("""
    <style>
        .title {
            font-size: 32px;
            color: #4CAF50;
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            font-size: 24px;
            color: #FF5722;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Welcome to the Crypto Quadratic Defender</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Encrypt and Decrypt Messages with a Quadratic Twist!</p>', unsafe_allow_html=True)

# Input Section
original_word = st.text_input("Enter a word or phrase to encrypt:", "")

if original_word:
    encrypted_word = julie_encrypt(original_word)
    decrypted_word = julie_decrypt(encrypted_word)

    # Display Results
    st.markdown("---")
    st.subheader("Results:")
    
    # Displaying the words with additional styling
    st.markdown(f"**Original Word:** `{original_word}`")
    st.markdown(f"**Encrypted Word:** `{encrypted_word}`")
    st.markdown(f"**Decrypted Word:** `{decrypted_word}`")

# Adding some extra information for the user
st.markdown("""
    <br>
    <p style="font-size: 16px; text-align: center;">The encryption technique here is based on modifying each character's ASCII value using the square of the word length.</p>
    <p style="font-size: 16px; text-align: center;">Feel free to try any string and watch the magic happen!</p>
""", unsafe_allow_html=True)
