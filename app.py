import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function To get response from LLAma 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model='C:/Users/YAS/Downloads/LLM/models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0})
    
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                            template=template)
    
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                    page_icon='📝',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 📝")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Academist', 'Researchers', 'Data Scientist', 'Freshers'), index=0)

# Custom CSS styles for button color
button_style = """
<style>
/* Change button color */
div[data-testid="stButton"] button {
    background-color: #ff6347; /* Coral color */
    color: #ffffff; /* White text color */
}
</style>
"""

# Inject custom CSS for button color
st.markdown(button_style, unsafe_allow_html=True)

submit = st.button("Generate")

# Final response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
