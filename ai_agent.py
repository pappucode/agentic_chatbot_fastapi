from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent 
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()



openai_llm = ChatOpenAI()
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

#search_tool = TavilySearch(max_results=5)
search_tool = DuckDuckGoSearchRun()


system_prompt = "You are a helpful assistant"

agent = create_agent(
    model = openai_llm,
    tools = [search_tool],
    system_prompt = system_prompt
)

query = "Obama's first name?"
state={"message":query}

response = agent.invoke(state)

print(response["messages"][-1].content)



