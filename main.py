import os   
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent

from src.prompt import system_prompt
from src.tools import get_weather


## Loading the API Key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def main():
    agent = create_agent(
        model="google_genai:gemini-2.5-flash",
        tools=[get_weather],
        system_prompt= system_prompt
    )

    user=input("Enter:")
    response = agent.invoke({"messages": [("user", user)]})
    content = response["messages"][-1].content

    if isinstance(content, list):
        print(content[0]["text"])
    else:
        print(content)
 

if __name__ == "__main__":
    main()
