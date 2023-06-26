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

    prompt_basic= PromptTemplate(
        input_variables=["input","history"],
        template='This is a prompt and we expect the input to be {input} and history to be {history}'
    )

    memory=ConversationEntityMemory(llm=llm)
    conversation_with_memory = ConversationChain(
        llm=llm, 
        verbose=True,
        prompt=prompt,
        memory=memory
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

    responses=[]
    for line in lines:
        variables=memory.load_memory_variables({"input": line})
        response=constitutional_chain.run(input=line,history=variables['history'], entities=variables["entities"])
        responses.append(response)

    for r in responses:
        print(r)