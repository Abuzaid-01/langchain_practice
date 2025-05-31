from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt = PromptTemplate(
    template = "tell me about this {topic}",
    input_variables = ["topic"]
)

out = StrOutputParser()

chain = prompt | model | out

result = chain.invoke({
    "topic" : "classical mechanics"

})

print(result) 

chain.get_graph().print_ascii()