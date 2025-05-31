from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")



chat = ChatPromptTemplate([
    ("system", "You are a helpful assistant in this domain {domain}"),
    ("user", "explain this topic in simple terms: {topic}")]
)

chain = chat | model


result = chain.invoke({
    "domain" : "Phsics",
    "topic" : "Bose-Einstein_theory"
})

print(result.content)