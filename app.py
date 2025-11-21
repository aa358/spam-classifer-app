import streamlit as st
import joblib

# Load model
model = joblib.load("email_spam_classifier.pkl")

st.title("📧 Email Spam Classifier")
st.write("Enter any email text and the model will predict whether it is spam or not.")

# User input
user_input = st.text_area("Email text:", height=200)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]

        if prediction == 1:
            st.error("🚨 This looks like **SPAM**!")
        else:
            st.success("✅ This looks **SAFE** (not spam).")
