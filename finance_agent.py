from dotenv import load_dotenv # for env variables
from phi.agent import Agent # create AI Agent
from phi.tools.yfinance import YFinanceTools # acccess to yahoo finance
from phi.model.openai import OpenAIChat # openai model
import os # interaction between os and env variables

# load env variables
load_dotenv()

# create finance agent
finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(
        id="gpt-4o",
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["API_KEY"]
    ),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True
        )
    ],
    instructions=[
        "Use tables to display data",
        "Always mention my name 'Julien' in your responses"
    ],
    show_tools_calls=True,
    markdown=True
)
finance_agent.print_response("Summarize the company news for Tesla", stream=True)