import os
import sys
from langchain import HuggingFaceHub
from authentication_secrets import *
from run_conversation import *

HUGGINGFACEHUB_API_TOKEN = hf_token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
os.environ["HUGGINGFACE_HUB_CACHE"] = '/scratch/jlb638/hf_cache'

repo_id = "facebook/opt-350m"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0})

conversation(llm, input_file=sys.argv[1])