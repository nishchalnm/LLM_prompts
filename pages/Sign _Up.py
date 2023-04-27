import streamlit as st
from sqllite_helper import *

def signup():
    st.title("Sign Up")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    signup_button = st.button("Sign Up")
    if signup_button:
        if password == confirm_password:
            user_flag = insert_into_user_table(username, email, password)
            if user_flag == 0:
                st.success("Signed up successfully!", icon="✅")
            else:
                st.warning('username is not available', icon="⚠️")
        else:
            st.warning('password does not match!', icon="⚠️")

    st.markdown('Already have an account? [Login](/Home)')

def main():
    signup()

if __name__ == '__main__':
    main()