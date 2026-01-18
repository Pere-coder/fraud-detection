import streamlit as st
from main import get_numerical_features


# Page configuration for a professional look
st.set_page_config(page_title="InstVerify", page_icon="🛡️", layout="centered")

# Custom CSS to make it look modern
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4F46E5; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ InstVerify")
st.markdown("### AI-Powered Instagram Fraud Detection")
st.info("Verify if an account is a bot, a scammer, or a genuine user.")

# Input Section
with st.container():
    acc_name = st.text_input("Enter Instagram Username", placeholder="")
    submit = st.button("Analyze Account")

if submit:
    if not acc_name:
        st.warning("Please enter a username.")
    else:
        with st.spinner(f"🔍 Analyzing @{acc_name}..."):
            try:
                # 1. Get features and predict
                 
                prediction = get_numerical_features(acc_name) # Should return 0 or 1
                
                st.divider()

                # 2. Hero Result Section
                if prediction == 1:
                    st.error(f"### 🚩 High Risk: Potential Fraud Detected")
                    st.write("Our AI model has flagged this account as highly suspicious.")
                else:
                    st.success(f"### ✅ Low Risk: Account Appears Genuine")
                    st.write("This account shows patterns consistent with real human activity.")

                # show_details = st.toggle('show details')

                # if show_details:
                #     st.write(prediction)
                # else:
                #     st.write('Toggle the box above to see the details.')

            except Exception as e:
                st.error(f"Error: Could not fetch data for @{acc_name}. Ensure the username is correct or try again later.")