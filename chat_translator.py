import os 

import getpass

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

if not "OPENAI_API_KEY" in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass(
        prompt= "Give you OPENAI_API_KEY :"
    )

from langchain.chat_models import init_chat_model

model = init_chat_model('gpt-4o-mini',model_provider='openai')

language = input("enter which language  do you want to translate")
userMessage = input('Enter the content to translate: ')

from langchain_core.prompts import ChatPromptTemplate

systemMessage = f"Translate english language into {language}: "
prompt_template = ChatPromptTemplate.from_messages(
    [
    ("system", systemMessage), ("user", userMessage)
]
)
prompt = prompt_template.invoke({"language":systemMessage,"text":userMessage})
converting_objToMessage = prompt.to_messages()

for token in model.stream(converting_objToMessage):
    print(token.content,end="")