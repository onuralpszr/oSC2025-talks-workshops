import os

from mcp import StdioServerParameters
from smolagents import CodeAgent, LiteLLMModel, ToolCollection

model = LiteLLMModel(
    model_id="ollama_chat/PetrosStav/gemma3-tools:4b",
    api_base="http://localhost:11434",
    api_key="openSUSE-is-awesome",
    num_ctx=8192,
)

server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with ToolCollection.from_mcp(
    {"url": "http://127.0.0.1:8000/mcp", "transport": "streamable-http"},
    trust_remote_code=True,
) as tool_collection:
    agent = CodeAgent(tools=[*tool_collection.tools], add_base_tools=True, model=model)
    agent.run("Please find a remedy for hangover.")
