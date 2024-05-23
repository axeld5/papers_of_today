"""Helper functions to facilitate langchain use and algorithm iterations"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_filtering_prompt():
    prompt = """You are being given the abstract of a paper. Is this paper about {topic}, or not?
    Answer "YES" if the abstract is related to {topic}, and "NO" otherwise.
    <abstract> {abstract} </abstract>
    Answer:"""
    return prompt

def make_chain(model, prompt:str):
    parser = StrOutputParser()
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", "You are an helpful AI assistant"), ("user", prompt)]
    )
    chain = prompt_template | model | parser
    return chain