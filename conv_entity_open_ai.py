import sys
from langchain.llms import OpenAI
from run_conversation import conversation
from authentication_secrets import *

llm = OpenAI(openai_api_key=openai_api_key)

conversation(llm, input_file=sys.argv[1])