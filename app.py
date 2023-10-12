import streamlit as stl
import openai

openai.api_key = stl.secrets["api_key"]

stl.title("Hello World!!")

with stl.form("form"):
    user_input = stl.text_input("Prompt")
    size = stl.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = stl.form_submit_button("Submit")
    
if submit and user_input:
    stl.write(user_input)
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail appeareance of the input. Response it shortly around 20 words"
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })

    with stl.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    stl.write(prompt)

    with stl.spinner("Waiting for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size
        )

    stl.image(dalle_response["data"][0]["url"])
    
