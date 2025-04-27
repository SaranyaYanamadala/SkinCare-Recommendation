from dotenv import load_dotenv
from pydantic import BaseModel
#from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from AI_agent.tools import search_tool, wiki_tool


## Load the environment variables
load_dotenv()

## Data Model
'''class ResearchResponse(BaseModel) :
    topic : str
    summary : str
    sources : list[str]
    tools_used : list[str]'''
    

## Set up an LLM
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

## Creating a parser
#parser = PydanticOutputParser(pydantic_object = ResearchResponse)

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            ## System message, information to the system
            "system",
            
            """
            You are a skincare expert. Based on the user's skin type and skin concern, suggest some active ingredients 
            that help the user get rid of that skin concern they have. Also generate some relevant recommendations for 
            the user's prompt particularly for women. Use the available tools to generate the relevant suggestions. 
            Use emojis to make the output good looking.
            
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)
#.partial(format_instructions = parser.get_format_instructions())

## Creating and running the agent
tools = [search_tool, wiki_tool]
agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)

## Agent : out agent, tools : tools we are using, verbose : see the thought process of the agent
## Execute the agent
def run_agent(user_prompt) :
    agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)
    
    return agent_executor.invoke({"query" : user_prompt})


def execute_agent(user_prompt) :
    raw_response = run_agent(user_prompt)
    try :
        #structured_response = parser.parse(raw_response.get("output"))
        structured_response = raw_response.get("output")
        return structured_response
        #print(structured_response)
    except Exception as e :
        print("Error parsing in response", e, "Raw response - ", raw_response)
        return None
        
#execute_agent("tips for dry skin")