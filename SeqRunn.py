from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
#  prompt template
prompt = PromptTemplate.from_template(
    "explain {topic} in simple terms"
)
# model 

model = ChatMistralAI(model="mistral-medium", temperature=0.9)
# output parser
parser = StrOutputParser()
#manual frolw step by step 
# make the chai

chain   = prompt | model | parser

# call the chain
#  

result = chain.invoke({"topic": "quantum computing"})
print(result)


