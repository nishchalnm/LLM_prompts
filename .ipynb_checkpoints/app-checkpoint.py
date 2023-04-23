import streamlit as st
import numpy as np
import pandas as pd
import os
import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from paraphraser import Paraphraser

st.title("Optimize your prompts for LLMs like Chat GPT")
st.text("Enter a question in your language and we will suggest 5 prompts that are optimized for the best resluts from LLMs like Chap GPT.")

# Create a text input for the user to enter their question
question = st.text_input("Enter your question here:")

# Initialize the paraphraser object
model_path = "/Users/nishchalmishra/Desktop/prompts"
paraphraser = Paraphraser(model_path, device ="cpu")

# Create a button to trigger the paraphrasing
if st.button("Paraphrase"):
    # Call the paraphrase function on the user input
    paraphrases = paraphraser.paraphrase(question)
    # Display the paraphrases
    for i, paraphrase in enumerate(paraphrases):
        st.write(f"Paraphrase {i+1}: {paraphrase}")


