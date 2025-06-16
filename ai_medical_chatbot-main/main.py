import base64
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os
import logging
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# API URL and Key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ API KEY is not set in the .env file")

def process_image(image_path=None, query=None):
    try:
        encoded_image = None
        image_mime = "image/jpeg"

        if image_path:
            with open(image_path, "rb") as image_file:
                image_content = image_file.read()
                encoded_image = base64.b64encode(image_content).decode("utf-8")

            try:
                img = Image.open(io.BytesIO(image_content))
                image_mime = Image.MIME.get(img.format, "image/jpeg")  # Determine image MIME type
                img.verify()
            except Exception as e:
                logger.error(f"Invalid image format: {str(e)}")
                return {"error": f"Invalid image format: {str(e)}"}

        # Construct messages
        messages = [{"role": "user", "content": [{"type": "text", "text": query}]}]

        if encoded_image:
            messages[0]["content"].append({
                "type": "image_url",
                "image_url": {"url": f"data:{image_mime};base64,{encoded_image}"}
            })

        def make_api_request(model):
            try:
                response = requests.post(
                    GROQ_API_URL,
                    json={
                        "model": model,
                        "messages": messages,
                        "max_tokens": 1000
                    },
                    headers={
                        "Authorization": f"Bearer {GROQ_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    timeout=30
                )
                return response
            except requests.RequestException as e:
                logger.error(f"Request failed for {model}: {str(e)}")
                return None

        # Query both models
        llama_11b_response = make_api_request("llama-3.2-11b-vision-preview")
        llama_90b_response = make_api_request("llama-3.2-90b-vision-preview")

        responses = {}
        for label, response in [("LLaMA 11B", llama_11b_response), ("LLaMA 90B", llama_90b_response)]:
            if response and response.status_code == 200:
                try:
                    result = response.json()
                    answer = result["choices"][0]["message"]["content"]
                    logger.info(f"Processed response from {label}: {answer[:100]}...")
                    responses[label] = answer
                except KeyError as e:
                    logger.error(f"Key error in response from {label}: {str(e)}")
                    responses[label] = f"Error parsing response: {str(e)}"
            else:
                error_code = response.status_code if response else "No response"
                logger.error(f"Error from {label}: {error_code}")
                responses[label] = f"Error from {label}: {error_code}"

        return responses

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"error": f"Unexpected error: {str(e)}"}

if __name__ == "__main__":
    # Example use
    image_path = "test0.png"  # Or set to None
    query = "What are the encoders in this picture?"

    result = process_image(image_path=image_path, query=query)
    print(json.dumps(result, indent=2))
