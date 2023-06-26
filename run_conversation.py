from langchain.prompts import PromptTemplate
from langchain.memory import ConversationEntityMemory
from langchain.chains import ConversationChain
from langchain.chains.constitutional_ai.base import ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple
def conversation(llm,input_file='input_basic.txt'):
    with open('template.txt', 'r') as file:
        template = file.read()

    prompt = PromptTemplate(
        input_variables=["history", "input","entities"],
        template=template
    )

    conversation_with_memory = ConversationChain(
        llm=llm, 
        verbose=True,
        prompt=prompt,
        memory=ConversationEntityMemory(llm=llm)
    )

    dramatic_principle = ConstitutionalPrinciple(
        name="Dramatic Principle",
        critique_request="The model should respond in a very dramatic, sensationalist way",
        revision_request="Rewrite the model's output to be very dramatic and sensationalist.",
    )

    constitutional_chain = ConstitutionalChain.from_llm(
        chain=conversation_with_memory,
        constitutional_principles=[dramatic_principle],
        llm=llm,
        verbose=True,
        )

    with open(input_file, 'r') as file:
        lines=file.readlines()

    for line in lines:
        response=conversation_with_memory.predict(input=line)
        #response=constitutional_chain.predict(line)
        print(response)