import json
import pandas as pd
import os
import traceback
import langchain_community
import langchain
from dotenv import load_dotenv

obj = langchain.chat_models.OpenAI()
load_dotenv()#load all env variables
key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key = key, model = "gpt-3.5-turbo", temperature = 0.5)
