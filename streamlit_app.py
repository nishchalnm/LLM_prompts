import openai
import streamlit as st
from transformers import AutoModel
from paraphraser import Paraphraser
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
device = "cpu"

def paraphrase_(input_text):
     model_path = "."
     paraphraser = Paraphraser(model_path, device=device)
     paraphrases = paraphraser.paraphrase(input_text)
     
     for i, paraphrase in enumerate(paraphrases):
         st.code(f"Paraphrase {i+1}: {paraphrase}")
        

st.title("Optimize your LLM Prompts")
st.subheader("Enter a promptand we will suggest 5 optimized prompts!!")
input_text = st.text_input( "Input Prompt", placeholder="how you doin? ", key="placeholder",)

login_button = st.button("Paraphrase")
if login_button:
   paraphrase_(input_text)

option = st.selectbox(
    'Select your choice of AI to look for the answers',
    ('chatGPT', 'Alpaca', 'BloombergGPT'))
if option == "chatGPT":
   openai.api_key = st.text_input( "OpenAI API key",)
else:
   openai.api_key = st.text_input( "API key",)

if openai.api_key is not None:
   def get_resp_from_openai():
      response = openai.ChatCompletion.create( model = "gpt-3.5-turbo", temperature = 0.2, max_tokens = 1000,
                     messages = [ {"role": "user", "content": input_text}])

      st.write(response['choices'][0]['message']['content'])
