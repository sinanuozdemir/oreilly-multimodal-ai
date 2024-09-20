import logging
import os

import openai
from dotenv import load_dotenv  # use .env
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

openai_api_key = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.route('/process_text', methods=['POST'])
def process_text():
    logging.info("Received request")
    data = request.json
    logging.debug(f"Request data: {data}")
    if 'text' not in data:
        logging.error("No text provided")
        return jsonify({"error": "No text provided"}), 400

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Keep all answers under 10 words."},
                {"role": "user", "content": data['text']}
            ],
            max_tokens=150
        )
        logging.debug(f"OpenAI response: {response}")
        return jsonify({"response": response.choices[0].message.content.strip()})
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
