from langchain.tools import tool 
@tool #decorator for the creating tool  
def get_greeting(name: str) -> str:
    """
    Generate aa greeting messagae for the user 
    """
    return f"Hello, {name}! Welcome to the world of AI tools!"

result = get_greeting.invoke({"name": "Alice"})
print(result)

print(get_greeting.name) # get the name of the tool
print(get_greeting.description) # get the description of the tool
print(get_greeting.args) 
