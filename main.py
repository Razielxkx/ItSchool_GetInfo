import streamlit as st
import requests

base_url = "http://127.0.0.1:9125"

btn_trainers = st.button("Get all trainers")
if btn_trainers:
    trainers = requests.get(f"{base_url}/trainers")
    st.dataframe(trainers.json())

trainer_name = st.text_input("Trainer name")
btn_search_trainer = st.button("Search trainer")
if btn_search_trainer:
    trainer = requests.get(f"{base_url}/trainers?name={trainer_name}")
    st.dataframe(trainer.json())

if __name__ == "__main__":
    trainers = requests.get(f"{base_url}/trainers")
    print(trainers.json())