import streamlit as st

# streamlit run app.py
st.title("Streamlit demo App for Machine Learning")

st.header("Heading of streamlit")

st.subheader("Sub-Heading of streamlit")

st.text("This is an example of text")

st.success("Success")

st.warning("warning")

st.info("information")

st.error("Error")

if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")

state= st.radio("What is your favourite color?",("Red","Green","Yello"))

if state=='Green':
    st.success("That's my favourite color as well!")


occupation = st.selectbox("What do you do?",
                          ["Student","vlogger","Engineer"])

st.text(f"slected option is {occupation}")

if st.button("Example Button"):
    st.error("You Clicked it")

st.sidebar.header("Heading of Sidebar")
st.sidebar.text("Sidebar TExt")