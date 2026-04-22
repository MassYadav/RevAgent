from dotenv import load_dotenv
load_dotenv()
from langchain_core.runnables import chain
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# component 
model = ChatMistralAI(model="mistral-medium", temperature=0.9)
parser  = StrOutputParser()

# two diffrent prompts
prompt1 = PromptTemplate.from_template(
    "explain {topic} in simple terms"
)
prompt2 = PromptTemplate.from_template(
    "what is {topic}?"
)

# input   
topic  = "quantum computing"

chain = RunnableParallel({

 "p1": prompt1 | model | parser,
 "p2": prompt2 | model | parser
})
result =chain.invoke({"topic": topic})
print(result)
