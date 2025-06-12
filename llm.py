import logging
import os
import requests

from pydantic import BaseModel
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

def extract_using_text(text: str, llm_model:str, feature_model: BaseModel):
    logger.info("Extracting using text.")

    url = f"https://ul-openai-api-dev.openai.azure.com/openai/deployments/{llm_model}/chat/completions?api-version=2024-10-01-preview"

    headers = {
        "Content-Type": "application/json",
        "api-key": os.getenv("AZURE_OPENAI_API_KEY")
    }

    data = {
        "messages": [
            {
                "role": "user", 
                "content": [
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "Extraction_Response",  # Add the name field explicitly
                "strict": True,
                "schema": feature_model.model_json_schema()
            }
        },
        "seed": 77,
        "temperature": 0,
        "stream": False
    }

    logger.info("Sending request to Azure OpenAI API.")
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        logger.error(f"API Error: {response.status_code} - {response.text}")

    response_json = response.json()
    logger.info("Response received from API.")
    model_string = response_json.get("choices", [])[0].get("message", {}).get("content", "{}")

    # create model instance from string
    model_instance = feature_model.model_validate_json(model_string)

    return model_instance