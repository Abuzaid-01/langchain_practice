from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt = PromptTemplate(
    template = "tell me a detailed report on {topic}",
    input_variables = ["topic"] 
)

prompt2 = PromptTemplate(
    template= "tell me six point summary on {topic}",
    input_variables=["topic"]   
)

out = StrOutputParser()

chain = prompt | model | out | prompt2 | model | out 

result = chain.invoke({
    "topic": "Independence Day of India"
})

print(result)

chain.get_graph().print_ascii()