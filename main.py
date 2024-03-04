# Building a Grammarly Lite App with Streamlit and Transformers

# Importing libraries
import streamlit as st
# from transformers import T5Tokenizer, T5ForConditionalGeneration
from happytransformer import HappyTextToText, TTSettings


# Defining the main function
def main():
    # Setting the title of the app
    st.set_page_config(page_title="Grammarly Lite App", page_icon=":books:")
    st.title("Grammarly Lite App")

    # Creating a text input box
    text = st.text_input("Enter text:")

    # Creating a button
    if st.button("Submit") | bool(text):
        # Tokenizing the input text
        tokenizer = HappyTextToText("T5","vennify/t5-base-grammar-correction")

        # Setting the parameters
        args = TTSettings(num_beams=2, min_length=1)

        # Generating the summary
        generated = tokenizer.generate_text(text, args=args)
        # Displaying the summary
        st.write("Your text: ")
        st.write(generated.text)


# Calling the main function
if __name__ == "__main__":
    main()
