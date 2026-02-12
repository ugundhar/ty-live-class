# Import statements
import os
from dotenv import load_dotenv
from gen_ai_hub.proxy.native.openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize the SAP AI Core OpenAI client
client = OpenAI()

query="what is the llm"
# Call GPT-4o
response = client.chat.completions.create(
    model_name="gpt-4o",
    messages=[
        {"role": "user", "content": query}
    ]
)

# Print the response
print(response.choices[0].message.content)