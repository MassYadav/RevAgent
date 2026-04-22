from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI

search_tpp = TavilySearchResults()
model = ChatMistralAI(model="mistral-medium", temperature=0.9)
prompt = PromptTemplate.from_template(
    "Summarize the following news article in one sentence: {article}"
)   
chain = prompt | model | StrOutputParser()
article = search_tpp.invoke({"query": "latest news on quantum computing"})
result = chain.invoke({"article": article})
print(result)
