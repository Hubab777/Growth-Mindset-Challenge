import streamlit as st

# Page config
st.set_page_config(page_title="growth mindset challenge")

# Custom CSS
st.markdown("""
    <style>
    /* Overall page styling */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Custom title style */
    .custom-title {
        color: #004d4d; !important; /* Dark Teal */
        font-size: 42px;
        text-align: center;
        font-weight: 700;
        margin-bottom: 25px;
    }

    /* Header style override */
    h2 {
        color: #00bfff !important; /* Sky Blue */
    }

    /* Footer style */
    .footer {
        color: #004d4d;
        font-size: 16px;
        text-align: center;
        margin-top: 50px;
        line-height: 1.6;
    }

    hr {
        border-top: 1px solid #bbb;
        margin-top: 40px;
    }

    /* Input and Text Area styling (optional extras) */
    .stTextInput > div > input,
    .stTextArea > div > textarea {
        background-color: #f0f8ff;
        border: 1px solid #a1c4fd;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Styled Title
st.markdown('<h1 class="custom-title">🌟Growth Mindset WebApp Challenge Using Streamlit🌟</h1>', unsafe_allow_html=True)

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements.")

# Quotes section
st.header("💡 Today's Growth Mindset Quote")
st.write("It's not that I'm so smart, it's just that I stay with problems longer. — Albert Einstein 🧠💡📈")

# Challenge input
st.header("📑What's Your Challenge Today?")
user_input = st.text_input("💭 Describe a challenge you are facing: ")

if user_input:
    st.success(f"You are facing: {user_input}. Keep trying and working smartly!🎯")
else:
    st.warning("🖋️ Tell us about your difficulty")

# Reflection section
st.header("🌠Reflect on your Learning")
reflection = st.text_area("✍🏻 Write Your Reflection here: ")

if reflection:
    st.success(f"✨Great Insight: Your Reflection: {reflection}")
else:
    st.info("💫 Reflection on past experience helps you grow! Share your difficulties.")

# Achievements section
st.header("🏆Celebrate Your Wins!")
achievements = st.text_input("💭 Share something you have recently accomplished:")

if achievements:
    st.success(f"🌟Amazing! You achieved: {achievements}")
else:
    st.info("Big or Small, every achievement counts👏🏻")

# Footer
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    🌱🚀💫 Every day is a chance to get better. <br>
    🎨🧩🌄 Great things are done by a series of small things brought together. — Vincent Van Gogh <br><br>
    <strong>©️ Created by Hubab Ikram</strong>
</div>
""", unsafe_allow_html=True)
