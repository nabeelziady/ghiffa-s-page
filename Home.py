import streamlit as st

st.set_page_config(
    page_title="All About You | Home",
    page_icon="❤️",
    layout="centered"
)

st.image("gipa2.jpg",
        use_container_width=True)
st.title("Welcome to Ghiffa's Page 💌🧚‍♀️💗")
st.subheader("The Prettiest • The Smartest • The Kindest • The Funniest • THE EVERYTHING!")
st.write("Naila Ghiffarissa, A SUPER AMAZING woman that always makes everyone amazed of how wonderful she is. Especially for her boyfriend , Nabeel, that endlessly falls in love with her everyday, everyhour, everyminute, everysecond, etc. She always makes his day better even when he's in his toughest time. He will always be thankful and grateful of how she can be his boyfriend. And he will always be proud of anything that she does because he always know that Ghiffa is the most amazing woman of all time.")

st.markdown("---")
st.header("How Pretty She Is?")
col1, col2, col3, = st.columns(3)
with col1:
    st.image("gipa1.jpg", use_container_width=True)
    st.image("gipa5.jpg", use_container_width=True)
    st.image("gipa8.jpg", use_container_width=True)
    st.image("gipa11.jpg", use_container_width=True)
with col2:
    st.image("gipa3.jpg", use_container_width=True)
    st.image("gipa6.jpg", use_container_width=True)
    st.image("gipa9.jpg", use_container_width=True)
    st.image("gipa12.jpg", use_container_width=True)
    st.image("gipa13.jpg", use_container_width=True)
with col3:
    st.image("gipa4.jpg", use_container_width=True)
    st.image("gipa7.jpg", use_container_width=True)
    st.image("gipa10.jpg", use_container_width=True)
    st.image("gipa14.jpg", use_container_width=True)

st.markdown("---")
st.caption("© 2025 All About You | Made with Streamlit & LOTS OF LOVEEEEEEEEEE")