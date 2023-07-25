from base import create_excel_agent
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

os.environ["OPENAI_API_KEY"] = "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"

agent = create_excel_agent(
    OpenAI(temperature=0),
    "titanic.xls",
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# agent.run("how many rows are there?")
agent.run("how many males with age more than 40 are there?")