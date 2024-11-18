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

# Streamlit App Configuration
st.set_page_config(page_title="CRYPTO QUADRATIC DEFENDER", page_icon="🔐", layout="centered")

# HTML and CSS for Background Video and Styling
st.markdown(
    f"""
    <style>
    body {{
        background-color: #000;
        color: white;
        font-family: 'Arial', sans-serif;
    }}
    [data-testid="stAppViewContainer"] {{
        background: url('https://cdn.pixabay.com/vimeo/204/204306/market-values-stock-exchange-720p.mp4') no-repeat center center fixed;
        background-size: cover;
    }}
    .title {{
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: white;
        margin-top: 20px;
    }}
    .subheader {{
        font-size: 24px;
        text-align: center;
        color: white;
    }}
    .info {{
        font-size: 16px;
        text-align: center;
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Header Section
st.markdown('<div class="title">CRYPTO QUADRATIC DEFENDER</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">ENCRYPT AND DECRYPT MESSAGES WITH MAXIMUM SECURITY</div>', unsafe_allow_html=True)

# Input Section
original_word = st.text_input("ENTER A WORD OR PHRASE TO ENCRYPT:", "").upper()

if original_word:
    encrypted_word = julie_encrypt(original_word)
    decrypted_word = julie_decrypt(encrypted_word)

    # Display Results
    st.markdown("---")
    st.markdown('<div class="subheader">RESULTS:</div>', unsafe_allow_html=True)
    st.markdown(f"**ORIGINAL WORD:** `{original_word}`")
    st.markdown(f"**ENCRYPTED WORD:** `{encrypted_word}`")
    st.markdown(f"**DECRYPTED WORD:** `{decrypted_word}`")

# Credits Section
st.markdown("---")
st.markdown(
    """
    <div class="info">
        THIS TOOL IS BASED ON A UNIQUE ENCRYPTION STANDARD DEVELOPED FOR SECURITY PURPOSES.<br>
        ALL RIGHTS RESERVED.<br><br>
        <strong>CREDITS:</strong> HARIHARAN M<br>
        COPYRIGHT 2024<br>
        CONTACT: 2011.HARIHARAN@GMAIL.COM
    </div>
    """,
    unsafe_allow_html=True
)
