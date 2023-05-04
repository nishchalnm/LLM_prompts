import streamlit as st
from sqllite_helper import *
from paraphraser import Paraphraser
device = "cpu"

def paraphrase_func():

    st.title("Optimize your LLM Prompts")
    st.text("Enter a promptand we will suggest 5 optimized prompts for the best resluts from LLMs.")
    #question = st.text_input( "Enter your Prompt!", placeholder="how you doin? ", key="placeholder",)
    #phrase = st.text_input("phrase")
    #p_button = st.button("pp")
    form = st.form(key='my_form')
    question = form.text_input("Enter your Prompt!", placeholder="how you doin? ", key="placeholder",)
    submit_button = form.form_submit_button(label='Paraphrase')
    #p_button = st.button("Paraphrase")
    print("p_button", submit_button)
    
    if submit_button:
        #st.session_state.p_button = True
        print("inside p_button", submit_button)
        model_path = "."
        paraphraser = Paraphraser(model_path, device=device)
        paraphrases = paraphraser.paraphrase(question)
        print("done")
        for i, paraphrase in enumerate(paraphrases):
            st.code(f"Paraphrase {i+1}: {paraphrase}")
        
paraphrase_func()