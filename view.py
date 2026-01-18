import streamlit as st
from main import get_numerical_features


st.title("InstVerify")
st.subheader("Type in the instagram handle or account name to verify if its fraud/bot or not")

with st.form(key = "search form"):
    acc_name = st.text_input("Search", "Instagram name")
    submit = st.form_submit_button("search")

if submit:
    with st.spinner("Searching"):
        action = get_numerical_features(acc_name)
    st.write(action)


