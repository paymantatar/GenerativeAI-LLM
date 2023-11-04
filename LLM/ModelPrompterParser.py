import os
import openai
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI()
chat

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )
# print(completion.choices[0].message)
# def get_completion(prompt, model=llm_model):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,
#     )
#     return response.choices[0].message["content"]

get_completion("What is 1+1?")

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

# customer_email = """
# Oefenen
# U kunt oefenen voor de examens op taalniveau A2, B1 en B2.
# Oefenen taalniveau B1 en B2
# Voor de taalexamens op taalniveau B1 en B2 (staatsexamen Nt2) zijn er oefenexamens. Er zijn ook losse oefenopdrachten voor Schrijven en Spreken op taalniveau B1. Ga naar de oefenexamens en oefenopdrachten
# """


style = """American English \
in a calm and respectful tone
"""

prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""

print(prompt)

response = get_completion(prompt)
response
