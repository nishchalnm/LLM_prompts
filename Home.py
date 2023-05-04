import os
import torch
import numpy as np
import pandas as pd
import streamlit as st
from sqllite_helper import *
from paraphraser import Paraphraser
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
device = "cpu"
from PIL import Image

# image = Image.open('para_logo.jpg')
# st.image(image, caption='Sunrise by the mountains')

def login():

    st.session_state = False
    authentication_status = False
    st.title("Login")
    username = st.text_input(label="**Username**")
    password = st.text_input("**Password**", type="password")
    login_button = st.button("Login")
    if login_button:
        username_in_db = 0
        check_flag = 0
        username_in_db = get_username(username)
        if username_in_db != 0:
            password_in_db, salt_str_in_db = get_password(username)
            password_hash = encrypt_password2(password, salt_str_in_db)
            if password_hash == password_in_db:
                st.success("Logged in successfully!")
                authentication_status = True
                st.session_state = True
            else:
                st.warning('Wrong password', icon="⚠️")
        else:
            st.warning('User is not registered!', icon="⚠️")
            st.markdown('Don\'t have an account? [Sign up](/Sign_Up)')
    else:
        st.markdown('Don\'t have an account? [Sign up](/Sign_Up)')
    return authentication_status


def main():
    st.set_page_config(page_title="Login/Sign Up", layout="wide", initial_sidebar_state="collapsed")

    st.markdown("""
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>""", unsafe_allow_html=True, )

    st.title("Welcome to Paraphrase!")
    
    authentication_status = login()
    #paraphrase_func()
    if authentication_status:
        st.header('Start Paraphrasing!!  [Move to Paraphrase Page](/paraphrase)')
        #st.warning('BLAH!!!')
            #paraphrase_func()
    else:
        st.warning('Not logged in', icon="⚠️")

#if __name__ == '__main__':
main()