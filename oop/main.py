import logging
import ollama

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Logging is now configured!")

# Constants

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "deepseek-r1:8b"


messages = [
    {"role": "system", "content": "You are an Sportive analyst, specialized in boxing."},
    {"role": "user", "content": "Tell me the five best Mexican boxers ever, please your response in Spanish."},
]

payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

response = ollama.chat(model=MODEL, messages=messages)
print(response['message']['content'])