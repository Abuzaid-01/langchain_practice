# from langchain_google_genai import ChatgoogleGenerativeAi
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain.schema.runnable import RunnableParallel
# from langchain_core.output_parsers import StrOutputParser

# model1 = ChatgoogleGenerativeAi(model="gemini-1.5-flash")

# prompt1 = PromptTemplate(
#     template = "genrate a notes from this {topic}",
#     input_variables = ["topic"]
# )


# prompt2 = PromptTemplate(
#     template = "generate a quiz on this {topic}",
#     input_variables = ["topic"]
# )

# prompt3 = PromptTemplate(
#     template = "merge the notes and quiz as notes == {notes} and quiz == {quiz}",
#     input_variables = ["notes", "quiz"]
# )


# out = StrOutputParser()

# parallel_chain = RunnableParallel({
#     'notes': prompt1 | model1 | out,
#     'quiz': prompt2 | model1 | out
# })

# merge_chain = prompt3 | model1 | out

# chain = parallel_chain | merge_chain

# result = chain.invoke({
#     "topic": "Quantum Mechanics"
# })
# print(result)
# chain.get_graph().print_ascii()