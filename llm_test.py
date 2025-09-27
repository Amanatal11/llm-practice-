from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

# Messages
messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What are variational autoencoders and list the top 5 applications for them?")
]

# Invoke
response = llm.invoke(messages)
print("🤖 Response:\n", response.content)

# Print full response object (with metadata)
print("\n📊 Full Response Object:\n", response)
