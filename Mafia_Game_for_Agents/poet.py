import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console  # ✅ import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console

# Init model
model_client = OpenAIChatCompletionClient(model="gpt-4o")

# Define agents
primary_agent = AssistantAgent(
    name="primary",
    model_client=model_client,
    system_message="You are a poetic assistant. Write poems with emotional depth and vivid imagery."
)

critic_agent = AssistantAgent(
    name="critic",
    model_client=model_client,
    system_message="You are a critic. Provide constructive feedback. Reply with 'APPROVE' if the poem is ready."
)

# Termination condition
text_termination = TextMentionTermination("APPROVE")

# Build team
team = RoundRobinGroupChat(
    [primary_agent, critic_agent],
    termination_condition=text_termination
)

# Streaming version
async def run_task_streaming(task: str):
    await team.reset()  # Clear prior state
    await Console(team.run_stream(task=task))  # Stream the messages to the console.
    async for message in team.run_stream(task=task):  # stream as it happens
        if isinstance(message, TaskResult):
            print(message.stop_reason)
        else:
            print(message)

if __name__ == "__main__":
    task = "Write a short poem about the fall season but also mention cats and remain elegant."
    asyncio.run(run_task_streaming(task))



