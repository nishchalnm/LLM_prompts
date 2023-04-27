import os
import torch
import numpy as np
import pandas as pd
import streamlit as st
from sqllite_helper import *
from paraphraser import Paraphraser
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
device = "cpu"



def login():
    authentication_status = False
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    if login_button:
        username_in_db = 0
        check_flag = 0
        username_in_db = get_username(username)
        if username_in_db != 0:
            password_hash = encrypt_password(password)
            password_in_db = get_password(username)
            if password_hash.decode('UTF-8') == password_in_db:
                st.success("Logged in successfully!")
                authentication_status = True
                st.session_state = True
                #st.sidebar.title(f"Welcome {username}")
                #paraphrase_func()
            else:
                st.warning('Wrong password', icon="⚠️")
        else:
            st.warning('User is not registered!', icon="⚠️")
    st.markdown('Don\'t have an account? [Sign up](/Sign_Up)')
    #return authentication_status

    def paraphrase_func():
        st.title("Optimize your LLM Prompts")
        st.text("Enter a promptand we will suggest 5 optimized prompts for the best resluts from LLMs.")
        question = st.text_input( "Enter your Prompt!", placeholder="how you doin? ", key="placeholder",)

        model_path = "."
        paraphraser = Paraphraser(model_path, device=device)
        p_button = st.button("Paraphrase")
        if p_button:
            paraphrases = paraphraser.paraphrase(question)
            print("done")
            for i, paraphrase in enumerate(paraphrases):
                st.code(f"Paraphrase {i+1}: {paraphrase}")

        option = st.selectbox( 'Select your choice of AI to look for the answers', ('chatGPT', 'Alpaca'))
        # if option == "chatGPT":
        #    openai.api_key = st.text_input( "OpenAI API key",)
        # else:
        #    openai.api_key = st.text_input( "API key",)

    paraphrase_func()

def main():
    st.set_page_config(page_title="Login/Sign Up", layout="wide")
    st.title("Welcome to Paraphrase!")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    login()
    # authentication_status = login()
    # if authentication_status:
    #     a = paraphrase_func()
    # else:
    #     st.warning('Not logged in', icon="⚠️")

if __name__ == '__main__':
    main()