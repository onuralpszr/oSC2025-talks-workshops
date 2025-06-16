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
    command="podman",
    args=[
        "run",
        "--rm",
        "--name",
        "redis-mcp-server",
        "-i",
        "-e",
        "REDIS_HOST=localhost",
        "-e",
        "REDIS_PORT=6379",
        "docker.io/mcp/redis:latest",
    ],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with ToolCollection.from_mcp(
    server_parameters, trust_remote_code=True
) as tool_collection:
    agent = CodeAgent(
        tools=[*tool_collection.tools],
        additional_authorized_imports=["redis"],
        add_base_tools=True,
        model=model,
    )
    agent.run("Can you search in redis for the key 'gecko' and return its value?")
