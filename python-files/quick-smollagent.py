from smolagents import CodeAgent, LiteLLMModel, WebSearchTool

model = LiteLLMModel(
    model_id="ollama_chat/PetrosStav/gemma3-tools:4b",
    api_base="http://localhost:11434",
    api_key="openSUSE-is-awesome",
    num_ctx=8192,
)

# ollama default is 2048 which will often fail horribly.
# 8192 works for easy tasks, more is better.
# Check https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator to
# calculate how much VRAM this will need for the selected model.

agent = CodeAgent(tools=[WebSearchTool()], model=model, stream_outputs=True)

agent.run(
    "How many seconds would it take for a leopard at full speed to run through Pont des Arts?"
)
