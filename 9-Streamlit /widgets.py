import streamlit as st
import pandas as pd


st.title("StreamLit Text Input")



name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age: ", 0,100,25)

st.write(f"Your age is {age}")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite langauge: ", options)
st.write(f"You selected {choice}.")



data = {
    "Name": ["Rachit", "Jane", "Jake", "Jill"], 
    "Age": [23,24,25,28],
    "City": ["Ghaziabad","Los Angeles","Chicago","Houston"]
}

df = pd.DataFrame(data)
df.to_csv("SampleData.csv")
st.write(df)


uploaded_file = st.file_uploader("chooose a csv file",type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
