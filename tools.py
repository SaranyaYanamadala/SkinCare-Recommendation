from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

## Saving to a file
def save_to_file(data : str, filename : str = "search_output.txt") :
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"---- Research Output ----\nTimestamp : {timestamp}\n\n\n{data}\n\n"
    
    with open(filename, "a", encoding = "utf-8") as file :
        file.write(formatted_text)
    
    return f"Data successfully saved to {filename}."

## Wrapping the function as a tool
save_tool = Tool(
    name = "save_text_to_file",
    func = save_to_file,
    description = "Saves the output of the search to a file.",
)

## Creating own custom tool, accessing DuckDuckGo
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name = "search",
    func = search.run,
    description = "Use this tool to fetch real-time information from the web, such as weather, current events, or anything that requires up-to-date data.",
)

## Wikipedia tool
api_wrapper = WikipediaAPIWrapper(top_k_results = 5, doc_content_chars_max = 80)
wiki_tool = WikipediaQueryRun(api_wrapper = api_wrapper)