from flask import Flask, request, jsonify
import os
from openai import OpenAI
import openai
import logging
logging.getLogger().setLevel(logging.INFO)

client = OpenAI()

app = Flask(__name__)
# openai.api_key = os.getenv('OPENAI_API_KEY')
# Route to accept user input and respond using OpenAI GPT
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input', '')
    # # logging.info(f"User input: {user_input}, datatype {type(user_input)}")
    # response = client.chat.completions.create(
    # model="gpt-4o",
    # messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {
    #             "role": "user",
    #             "content": f"{user_input}"
    #         }
    #     ]
    # )

    # # Extract and return the GPT response
    # gpt_response = response.choices[0].message.content
    # logging.info(f"GPT Response: {gpt_response}")
    return jsonify({'response': user_input})

@app.route('/')
def top_level_chat():
    user_input = 'static test output'
    # # logging.info(f"User input: {user_input}, datatype {type(user_input)}")
    # response = client.chat.completions.create(
    # model="gpt-4o",
    # messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {
    #             "role": "user",
    #             "content": f"{user_input}"
    #         }
    #     ]
    # )

    # # Extract and return the GPT response
    # gpt_response = response.choices[0].message.content
    # logging.info(f"GPT Response: {gpt_response}")
    return jsonify({'response': user_input})
if __name__ == "__main__":
    app.run(debug=True)