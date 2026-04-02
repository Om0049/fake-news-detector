import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    import re
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

st.title("Fake News Detection")

input_text = st.text_area("Enter News Text")

if st.button("Predict"):
    text = clean_text(input_text)
    text = vectorizer.transform([text])
    pred = model.predict(text)

    if pred[0] == 1:
        st.success("REAL NEWS")
    else:
        st.error("FAKE NEWS")