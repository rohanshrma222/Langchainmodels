from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.5, max_completion_tokens=10)
response = chat.invoke("Hello, how are you?")

print(response)  