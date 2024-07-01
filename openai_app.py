from openai_utils import generate_response
import streamlit as st




def main():
    st.title("My chatbot")
    
    question = st.text_input("Type your question here")
    

main()